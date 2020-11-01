from app import db
from app.models.checks import Check

class ChecksController:
    @staticmethod
    def new(parameters):
        # See if check name is not duplicate for this course
        if not Check.query.filter_by(name=parameters['name'], course_id = parameters['course_id']).first():
            # Create a new entry (record) for checks table and save to db
            check = Check(parameters['name'], int(parameters['course_id']), parameters['language'], parameters['start_date'], parameters['end_date'], parameters['interval'], True)
            db.session.add(check)
            db.session.commit()
        else: 
            # Raise value error if duplicate check name for this course 
            raise ValueError("Check name '{}' for course {} already exists.".format(parameters['name'], parameters['course_id']))

    @staticmethod
    def run(parameters):
        # Download the latest submissions
        check = Check.query.filter_by(id = parameters["check_id"]).first()
        if check:
            # check.download_submissions()
            return check.run_check(check.language, check.download_submissions())
        else:
            raise ValueError("Check with id {} is not present.".format(parameters["check_id"]))
