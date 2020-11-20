from app import db
from app.models.courses import Course
from app.models.users import User

class CourseController:
    @staticmethod
    def new(parameters):
        # Check if course name is not duplicate, save if not
        if not Course.query.filter_by(name=parameters['name']).first():
            # Create a new entry for course table and save to db
            course = Course(parameters['user_id'], parameters['name'])
            db.session.add(course)
            db.session.commit()
        else: 
            # Raise value error if duplicate course name
            raise ValueError("Course name '{}' already exists".format(parameters['name']))

    # List course names according to user ID
    def show_courses(parameters):
        is_admin = parameters.get('admin')
        user_id = parameters.get('user_id')
        course_names = []
        # Fetch all courses if admin
        if is_admin == "1":
            courses = Course.query.all()
        # Only fetch courses corresponding to given user ID
        else:
            courses = Course.query.filter_by(user_id = parameters.get('user_id'))
        for course in courses:
            course_names.append(course.name)
        return course_names