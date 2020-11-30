from app import db, scheduler
from app.models.checks import Check
from app.controllers.submissions_controller import SubmissionController
from app.controllers.reports_controller import ReportsController
from app.utils.csv_parser import parse
from datetime import datetime

class ChecksController:
    @staticmethod
    def new(parameters,file=None):
        # See if check name is not duplicate for this course
        if not Check.query.filter_by(name=parameters['name'], course_id = parameters['course_id']).first():
            # Create a new entry (record) for checks table and save to db
            
            check = Check(parameters['name'], int(parameters['course_id']), parameters['language'], parameters['start_date'], parameters['end_date'], parameters['interval'], True)
            db.session.add(check)
            db.session.commit()
            scheduler.add_job(func = ChecksController.run, trigger = "interval", hours = check.interval, args = [check.id], start_date = check.start_date, end_date = check.end_date)
            # scheduler.add_job(func = ChecksController.run, trigger = "interval", hours = 1, args = [1], next_run_time=datetime.now())

        else: 
            # Raise value error if duplicate check name for this course 
            raise ValueError("Check name '{}' for course {} already exists.".format(parameters['name'], parameters['course_id']))
        
        curr_check = Check.query.filter_by(name=parameters['name'], course_id = parameters['course_id']).first()
        if curr_check:
            duplicates = SubmissionController.new({'check_id':curr_check.id, 'header':parameters['header']},file)
        
    @staticmethod
    def show_checks(parameters):
        course_id = parameters.get('course_id')
        checks_list = []
        # Fetch checks corresponding to given course ID
        checks = Check.query.filter_by(course_id = course_id)
        for check in checks:
            checks_list.append({'id':check.id, 'name' : check.name, 'language' : check.language, 'start_date' : check.start_date})
        return checks_list


    @staticmethod
    def run(check_id):
        # print(parameters)
        # Download the latest submissions
        check = Check.query.filter_by(id = check_id).first()
        if check:
            report = ReportsController.new(check_id, datetime.now(), "")
            directories = check.download_submissions()
            url = check.run_check(check.language, directories)
            check.remove_submissions()
            print("Run end")
            print(url)
            if len(url) > 0:
                report.status = True
                report.report_link += url
                db.session.add(report)
                db.session.commit()
            return url
        else:
            raise ValueError("Check with id {} is not present.".format(check_id))
