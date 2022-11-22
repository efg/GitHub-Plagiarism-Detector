from flask import request, send_from_directory
from app import get_app
from app.utils.response import make_response
from app.controllers.courses_controller import CourseController
from app.controllers.users_controller import UserController
from app.controllers.submissions_controller import SubmissionController
from app.controllers.checks_controller import ChecksController
from app.controllers.paths_controller import PathsController
from app.controllers.reports_controller import ReportsController
from app.controllers.similarities_controller import SimilaritiesController


app = get_app()

# Default path


@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    return '<br>&nbspHello World, Flask lives here.'

# ----------------Course------------------------
# Add new course


@app.route('/course/new', methods=['post'])
def course_new():
    try:
        print(request.get_json())
        CourseController.new(request.get_json())
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success'), 200

# List course names for a user


@app.route('/course/list', methods=['get'])
def course_show():
    try:
        courses = CourseController.show_courses(request.args)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', courses), 200


# ----------------User------------------------
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

# Login


@app.route('/user/login', methods=['post'])
def user_login():
    try:
        user_data = UserController.login(request.get_json())
    except (ValueError, KeyError) as e:
        print(e)
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', user_data), 200


# ----------------Submissions------------------------
# Add a new list of submissions
# duplicate entries will not be added and will be returned to the caller in a form of list
@app.route('/submission/new', methods=['post'])
def submission_new():
    try:
        duplicate_entries = SubmissionController.new(
            request.form, request.files)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', duplicate_entries), 200

# Get all the submssions according to provided check_id


@app.route('/submission/list', methods=['get'])
def submission_list():
    try:
        list_of_submissions = SubmissionController.list_submissions(
            request.values)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', list_of_submissions), 200


# ----------------Checks------------------------
# Add a new check
@app.route('/check/new', methods=['post'])
def check_new():
    try:
        # print(request.form)
        ChecksController.new(request.form, request.files)
    except (ValueError, KeyError) as e:
        print("error", e)
        return make_response(e.args[0]), 400
    except Exception as e:
        print(e)
        return make_response('Server Error'), 500

    return make_response('Success'), 200

# List checks for a course


@app.route('/check/list', methods=['get'])
def checks_show():
    try:
        checks = ChecksController.show_checks(request.args)
    except (ValueError, KeyError) as e:
        print(e.args[0])
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', checks), 200

# Run the check with given check_id


@app.route('/check/run', methods=['post'])
def check_run():
    try:
        url = ChecksController.run(request.form)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', url), 200

# Delete the check with given id


@app.route('/check/delete', methods=['get'])
def delete_check():
    print(request.args)
    try:
        list_checks = ChecksController.delete_check(request.args)
        print("from delete_check", list_checks)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', list_checks), 200


# Enable a disabled check
@app.route('/check/enable', methods=['get'])
def enable_check():
    print(request.args)
    try:
        ChecksController.enable_check(request.args)
    except (ValueError, KeyError) as e:
        print(e)
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', True), 200

# Disable a check
@app.route('/check/disable', methods=['get'])
def disable_check():
    print(request.args)
    try:
        ChecksController.disable_check(request.args)
    except (ValueError, KeyError) as e:
        print(e)
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', True), 200

# Get status of the Check
@app.route('/check/status', methods=['get'])
def status_check():
    print(request.args)
    try:
        status = ChecksController.get_status(request.args)
    except (ValueError, KeyError) as e:
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', status), 200


# ----------------------Reports------------------------
# Get reports for a check id


@app.route('/report/list', methods=['get'])
def reports_show():
    try:
        reports = ReportsController.show_reports(request.args)
        # print(reports)
    except (ValueError, KeyError) as e:
        print(e.args[0])
        return make_response(e.args[0]), 400
    except Exception as e:
        return make_response('Server Error'), 500

    return make_response('Success', reports), 200

# Create new entry in reports table


@app.route('/report/new', methods=['post'])
def report_new():
    try:
        ReportsController.new(request.form)
    except (ValueError, KeyError) as e:
        print("error", e)
        return make_response(e.args[0]), 400
    except Exception as e:
        print(e)
        return make_response('Server Error'), 500

    return make_response('Success'), 200


# Create new entry in reports table
@app.route('/path/new', methods=['post'])
def path_new():
    try:
        PathsController.new(request.form, request.files)
    except (ValueError, KeyError) as e:
        print("error", e)
        return make_response(e.args[0]), 400
    except Exception as e:
        print(e)
        return make_response('Server Error'), 500

    return make_response('Success'), 200

# ----------------------Similarities (MOSS info)------------------------


@app.route('/check/similarities', methods=['get'])
def fetch_all_report_infos():
    try:
        MOSS_info = SimilaritiesController.fetch_all_report_info(request.args)
        # print(MOSS_info)

    except Exception as e:
        print(e)
        return make_response('Server Error'), 500

    return make_response('suceess', MOSS_info), 200

@app.route('/check/download', methods=['get'])
def download_report():
    file_name = ""
    file_path = ""
    try:
        file_path, file_name = ChecksController.download_check_details(request.args)
    except Exception as e:
        print(e)
        return make_response('Server Error'), 500

    response = send_from_directory(directory=file_path, path=file_name, as_attachment=True)
    return response