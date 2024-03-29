from app import db, scheduler
from datetime import datetime, timedelta
from app.models.check import Check
from app.models.report import Report
from pyexcel_xls import save_data

import os

from app.controllers.submissions_controller import SubmissionController
from app.controllers.reports_controller import ReportsController
from app.controllers.similarities_controller import SimilaritiesController

from app.utils.scrape import scrape_MOSS_report

from datetime import datetime
from collections import OrderedDict


class ChecksController:

    # This method fetches all the check details and dumps it into an .xls file.
    # This method returns the path and the name of the excel file.
    @staticmethod
    def download_check_details(parameters):
        check_id = parameters.get('check_id')
        moss_info = SimilaritiesController.get_moss_info(check_id=check_id)
        data = []
        for _, reports in moss_info.items():
            for report in reports:
                run_id = int(report['report_id'])
                repo_a = report['repo1']
                repo_b = report['repo2']
                shared_code_a_to_b = str(int(report['dupl_code1'])) + "%"
                shared_code_b_to_a = str(int(report['dupl_code2'])) + "%"
                similarity_jump_a_to_b = report['similarity_jump1']
                similarity_jump_b_to_a = report['similarity_jump2']

                list = [run_id, repo_a, repo_b, shared_code_a_to_b, shared_code_b_to_a, similarity_jump_a_to_b, similarity_jump_b_to_a] 

                data.append(list)
        sorted(data, key=lambda x:x[0], reverse=True)
        data.insert(0, ["Run ID", "Team A", "Team B", "Shared Code Repo A to B", "Shared Code Repo B to A", "Similarity Jump Repo A to B", "Similarity Jump Repo B to A"])
        data_to_csv = OrderedDict()
        data_to_csv.update({"Sheet 1": data})

        file_path = os.path.join(os.path.dirname(
            os.path.realpath('__file__')), 'app/files/',)
        file_name = "report.xls"

        save_data(file_path + file_name, data)

        return file_path, file_name



    """
    This method adds a job to the scheduler.

    Parameters:
    1. start_date: Indicates when the MOSS scheduled job should start.
    2. end_date: Indicates when the MOSS scheduled job should be terminated.
    3. check_id: The check Id for which a job has to be scheduler.
    4. hours_between_run: Indicates the interval between two consecutive triggers.
    5. offset: This value will be added to the end_date of the check. This is used to avoid 
               errors when professor extends the deadline of a submission.
    """
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
    
    # This method is used to remove job from the scheduler based on check_id
    @staticmethod
    def remove_scheduled_job(check_id):
        jobs = scheduler.get_jobs()
        print(jobs)
        scheduler.remove_job(str(check_id))

    # All the parameters from the HTTP request will be parsed and stored to the database.
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
            'header': parameters['header'],
            'interval': parameters['interval']},
            files)

        ChecksController.schedule_job(datetime.now(), curr_check.end_date, curr_check.id,)

    # This method compares all the submissions using the MOSS API.
    @staticmethod
    def run(check_id):
        # Download the latest submissions
        check = Check.query.filter_by(id=check_id).first()
        print("\n\nInside check run:  ", check_id)
        if check:
            report = ReportsController.new(check_id, datetime.now(), "")
            directories = check.download_submissions(check_id)
            url = check.run_check(check.language, directories)
            check.remove_submissions()
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

    
    # This method returns a list of all the checks based on the course_id.
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

    # This disables the check from triggering MOSS and 
    # also sets visibility to false in the database.
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

    # This method resumes triggering MOSS for the check_id passed.
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
                

    # This method disables the check from triggering MOSS based on the check_id passed.
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

    # This method returns the status of the check.
    @staticmethod
    def get_status(parameters):
        check_id = parameters.get('check_id')
        check = Check.query.filter_by(id=check_id,
                                      visibility="yes").first()
        if check:
            return {"status": check.is_active}
        raise Exception("CheckId not found")


