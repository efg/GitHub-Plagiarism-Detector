from app import db
from app.models.courses import Course

class CourseController:
    @staticmethod
    def new(parameters):
        # Check if course name is not duplicate and then save
        if not Course.query.filter_by(name=parameters['name']).first():
            # Create a new entry for course table and save to db
            course = Course(parameters['name'])
            db.session.add(course)
            db.session.commit()
        else: 
            # Duplicate course name raise value error
            raise ValueError("Course name '{}' already exists".format(parameters['name']))