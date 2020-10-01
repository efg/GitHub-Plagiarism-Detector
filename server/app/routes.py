from flask import request
from app import get_app
from app.utils.response import make_response
from app.controllers.courses_controller import CourseController

app = get_app()

@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    return '<br>&nbspHello World, Flask lives.'

@app.route('/course/new', methods=['get', 'post'])
def course_new():
    try:
        CourseController.new(request.args)
    except ValueError as e: 
        return make_response(e.args), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success'), 200