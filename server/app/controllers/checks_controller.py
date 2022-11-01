from app import db, scheduler
from datetime import datetime, timedelta
from app.models.check import Check
from app.models.report import Report

import os

from app.controllers.submissions_controller import SubmissionController
from app.controllers.reports_controller import ReportsController
from app.controllers.similarities_controller import SimilaritiesController

from app.utils.scrape import scrape_MOSS_report

from datetime import datetime


class ChecksController:

    @staticmethod
    def schedule_job(start_date, end_date, check_id, hours_between_run=12, offset=5):
        scheduler.add_job(
            func=ChecksController.run,
            trigger="interval",
            hours=hours_between_run,
            args=[check_id],
            id=str(check_id),
            end_date=end_date + timedelta(days=offset),
            next_run_time=start_date)
    
    @staticmethod
    def remove_scheduled_job(check_id):
        jobs = scheduler.get_jobs()
        print(jobs)
        scheduler.remove_job(str(check_id))

    @staticmethod
    def new(parameters, files=None):
        # See if check name is not duplicate for this course
        if not Check.query.filter_by(name=parameters['name'],
                                     course_id=parameters['course_id']).first():
            # Create a new entry (record) for checks table and save to db
            check = Check(parameters['name'],
                          int(parameters['course_id']),
                          parameters['language'],
                          datetime.strptime(
                              str(parameters['start_date']), "%Y-%m-%d"),
                          datetime.strptime(
                              str(parameters['end_date']), "%Y-%m-%d"),
                          parameters['interval'], True, "yes")
            db.session.add(check)
            db.session.commit()
            # scheduler.add_job(func = ChecksController.run, trigger = "interval", hours = check.interval, args = [check.id], start_date = check.start_date, end_date = check.end_date)

        else:
            # Raise value error if duplicate check name for this course
            raise ValueError("Check name '{}' for course {} already exists.".format(
                parameters['name'], parameters['course_id']))

        curr_check = Check.query.filter_by(name=parameters['name'],
                                           course_id=parameters['course_id']).first()

        if curr_check == None:
            print(">>>> Error..inserting data!")
            return

        SubmissionController.new({
            'check_id': curr_check.id,
            'header': parameters['header']},
            files)

        ChecksController.schedule_job(datetime.now(), curr_check.end_date, curr_check.id,)

        # scheduler.add_job(
        #     func=ChecksController.run,
        #     trigger="interval",
        #     hours=hours_between_run,
        #     args=[curr_check.id],
        #     id=curr_check.id,
        #     end_date=curr_check.end_date + timedelta(days=offset),
        #     next_run_time=datetime.now())

    @staticmethod
    def run(check_id):
        # Download the latest submissions
        check = Check.query.filter_by(id=check_id).first()
        #ChecksController.disable_check(check_id)
        #ChecksController.enable_check(check_id)
        print("\n\nInside check run:  ", check_id)
        if check:
            report = ReportsController.new(check_id, datetime.now(), "")
            directories = check.download_submissions(check_id)
            url = check.run_check(check.language, directories)
            check.remove_submissions()
            # url = "http://moss.stanford.edu/results/0/8842422701801"  # TODO: remove this line
            print("\n\n >>> Run end", url)

            if url and len(url) > 0:
                report.status = True
                report.report_link += url
                db.session.add(report)
                db.session.commit()

                # pass this url for scraping and print result
                try:
                    # get info by scrpaing the MOSS report
                    html = ""
                    MOSS_info = scrape_MOSS_report(url)
                    print(MOSS_info)
                    reports = Report.query.filter_by(check_id=check_id).all()
                    if reports:
                        SimilaritiesController.new(
                            check.id, reports[-1].id, MOSS_info)
                        #calculate and send email to the instructor about highest jumps after this run
                        report.calculateJumps(check.id, reports[-1].id, MOSS_info)

                    else:
                        raise ValueError("Report does not exist!")
                except Exception as e:
                    print("\n\nScraping failed due to ", e)

            else:
                raise ValueError("\nError >>> No URL\n")
            return url
        else:
            raise ValueError(
                "Check with id {} is not present.".format(check_id))

    @staticmethod
    def show_checks(parameters):

        course_id = parameters.get('course_id')
        checks_list = []
        # Fetch checks corresponding to given course ID
        checks = Check.query.filter_by(course_id=course_id,
                                       visibility="yes")
        for check in checks:
            checks_list.append({'id': check.id,
                                'name': check.name,
                                'language': check.language,
                                'is_active': check.is_active,
                                'start_date': check.start_date.date()})
        return checks_list

    @staticmethod
    def delete_check(parameters):
        print("\n inside delete check", parameters)
        check_id = parameters.get('check_id')
        course_id = parameters.get('course_id')
        # Mark the check as not visible
        check = Check.query.filter_by(id=check_id,
                                      visibility="yes").first()
        print("\n->", check)
        if check:
            check.visibility = "no"
            db.session.commit()
            return ChecksController.show_checks({'course_id': course_id})
        return []

    @staticmethod
    def enable_check(parameters):
        check_id = parameters.get('check_id')
        check = Check.query.filter_by(id=check_id,
                                      visibility="yes").first()
        if check:
            if not check.is_active:
                check.is_active = True
                db.session.commit()
                ChecksController.schedule_job(datetime.now(), check.end_date, check_id,)
                

    @staticmethod
    def disable_check(parameters):
        print("\n inside disable check", parameters)
        check_id = parameters.get('check_id')
        check = Check.query.filter_by(id=check_id,
                                      visibility="yes").first()
        if check:
            if check.is_active:
                check.is_active = False
                db.session.commit()
                ChecksController.remove_scheduled_job(check_id)

    @staticmethod
    def get_status(parameters):
        check_id = parameters.get('check_id')
        check = Check.query.filter_by(id=check_id,
                                      visibility="yes").first()
        if check:
            return {"status": check.is_active}
        raise Exception("CheckId not found")


