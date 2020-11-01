from flask import request
from app import get_app
from app.utils.response import make_response
from app.controllers.courses_controller import CourseController
from app.controllers.users_controller import UserController
from app.controllers.submissions_controller import SubmissionController
from app.controllers.checks_controller import ChecksController


app = get_app()

#Default path
@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    return '<br>&nbspHello World, Flask lives.'

# Add new course
@app.route('/course/new', methods=['post'])
def course_new():
    try:
        CourseController.new(request.form)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success'), 200

# List course names for a user
@app.route('/course/list', methods=['get'])
def course_show():
    try:
        courses = CourseController.show_courses(request.values)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', courses), 200

# Add new user
@app.route('/user/new', methods=['post'])
def user_new():
    try:
        UserController.new(request.form)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500
    
    return make_response('Success'), 200

#Add a new list of submissions
#duplicate entries will not be added and will be returned to the caller in a form of list
@app.route('/submission/new', methods=['post'])
def submission_new():
    try:
        duplicate_entries = SubmissionController.new(request.form, request.files)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500
    
    return make_response('Success', duplicate_entries), 200


#Add a new check
@app.route('/check/new', methods=['post'])
def check_new():
    try:
        ChecksController.new(request.form)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500
    
    return make_response('Success'), 200

# Get all the submssions according to provided check_id
@app.route('/submission/list', methods=['get'])
def submission_list():
    try:
        list_of_submissions = SubmissionController.list_submissions(request.values)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500
    
    return make_response('Success', list_of_submissions), 200