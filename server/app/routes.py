from flask import request
from app import get_app
from app.utils.response import make_response
from app.controllers.courses_controller import CourseController
from app.controllers.users_controller import UserController
from app.controllers.submissions_controller import SubmissionController

app = get_app()

@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    return '<br>&nbspHello World, Flask lives.'

@app.route('/course/new', methods=['post'])
def course_new():
    try:
        CourseController.new(request.args)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success'), 200

@app.route('/user/new', methods=['post'])
def user_new():
    try:
        UserController.new(request.args)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500
    
    return make_response('Success'), 200

@app.route('/submission/new', methods=['post'])
def submission_new():
    try:
        duplicate_entries = SubmissionController.new(request.form, request.files)
    except (ValueError, KeyError) as e:
        print(e)
        return make_response(e.args[0]), 400
    except Exception as e:
        print(e)
        return make_response('Server Error'), 500
    
    return make_response('Success', duplicate_entries), 200