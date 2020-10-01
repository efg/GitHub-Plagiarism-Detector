from app import db
from app.models.checks import Check

class ChecksController:
    @staticmethod
    def new(parameters):
        # Check if check name is not duplicate and then save
        if not Check.query.filter_by(name=parameters['name'], course_id = parameters['course_id']).first():
            # Create a new entry for checks table and save to db
            check = Check(parameters['name'], int(parameters['course_id']), parameters['start_date'], parameters['end_date'], parameters['interval'], True)
            db.session.add(check)
            db.session.commit()
        else: 
            # Duplicate course name raise value error
            raise ValueError("Check name '{}' for course {} already exists.".format(parameters['name'], parameters['course_id']))