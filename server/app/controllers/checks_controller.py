from app import db, scheduler
from app.models.checks import Check
from app.controllers.submissions_controller import SubmissionController
# import datetime

class ChecksController:
    @staticmethod
    def new(parameters):
        # See if check name is not duplicate for this course
        if not Check.query.filter_by(name=parameters['name'], course_id = parameters['course_id']).first():
            # Create a new entry (record) for checks table and save to db
            
            # scheduler.add_job(func = ChecksController.test, trigger = "interval", minutes = 1, args = {"check_id" : 1}, next_run_time=datetime.datetime.now())
            # scheduler.start()
            check = Check(parameters['name'], int(parameters['course_id']), parameters['language'], parameters['start_date'], parameters['end_date'], parameters['interval'], True)
            db.session.add(check)
            db.session.commit()
        else: 
            # Raise value error if duplicate check name for this course 
            raise ValueError("Check name '{}' for course {} already exists.".format(parameters['name'], parameters['course_id']))
        
        curr_check = Check.query.filter_by(name=parameters['name'], course_id = parameters['course_id']).first()
        if curr_check:
            SubmissionController.new({'check_id':curr_check.id, 'header':False},parameters['csvFile'])

    @staticmethod
    def run(parameters):
        # Download the latest submissions
        check = Check.query.filter_by(id = parameters["check_id"]).first()
        if check:
            directories = check.download_submissions()
            url = check.run_check(check.language, directories)
            check.remove_submissions()
            return url
        else:
            raise ValueError("Check with id {} is not present.".format(parameters["check_id"]))
