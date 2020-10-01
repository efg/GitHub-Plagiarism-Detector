from app import db
from app.models.courses import Course
from app.models.users import User

class CourseController:
    @staticmethod
    def new(parameters):
        # Check if course name is not duplicate and then save
        if not Course.query.filter_by(name=parameters['name']).first():
            # Create a new entry for course table and save to db
            course = Course(parameters['user_id'], parameters['name'])
            db.session.add(course)
            db.session.commit()
        else: 
            # Duplicate course name raise value error
            raise ValueError("Course name '{}' already exists".format(parameters['name']))

    def show_courses(parameters):
        is_admin = parameters['admin']
        user_id = parameters['user_id']
        course_names = []
        if is_admin == "true":
            courses = Course.query.all()
        else:
            courses = Course.query.filter_by(user_id = parameters['user_id'])
        for course in courses:
            course_names.append(course.name)
        return course_names