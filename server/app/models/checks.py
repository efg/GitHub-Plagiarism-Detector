import logging
import os
import shutil

import git
import mosspy
from app import db
from app.utils.directories import extract_files_from_dir
from app.utils.languages import get_file_extensions
from dotenv import load_dotenv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


from app.models.submissions import Submission

load_dotenv()


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Check(db.Model):
    __tablename__ = 'checks'

    id = db.Column(db.Integer,
                   primary_key=True)
    course_id = db.Column(db.Integer,
                          db.ForeignKey("courses.id",
                                        ondelete='CASCADE'),
                          nullable=False)
    name = db.Column(db.String(64), nullable=False)
    language = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    # Time interval after which to run the check again
    interval = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, nullable=False)
    visibility = db.Column(db.String(10), nullable=False)
    
    paths = db.relationship('Path', backref='checks', lazy=True)
    submissions = db.relationship('Submission', backref='checks', lazy=True)

    def __init__(self, name, 
                course_id, 
                language, 
                start_date, 
                end_date, 
                interval, 
                is_active=True,
                visibility="yes"):
        self.name = name
        self.course_id = course_id
        self.language = language
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.is_active = is_active
        self.visibility = visibility

    def __repr__(self) -> str:
        return f"{self.name} {self.course_id} {self.language}"

    # Returns the check directory path - <course_id>_<db_id>_<check_name>
    def get_check_dir_path(self):
        files_path = os.path.join(os.path.dirname(
            os.path.realpath('__file__')), 'app/files/')
        check_dir_name = '{}_{}_{}'.format(self.course_id, self.id, self.name)
        check_dir_path = os.path.join(files_path, check_dir_name)
        return check_dir_path

    def get_all_submissions(self, check_id):
        return Submission.query.filter_by(id=check_id).all()

    # Download github repositories and return the downloaded directory list
    # Each check will create its own sub-folder in /app/files and clone all repositories in it
    def download_submissions(self, check_id):
        directories = []
        check_dir_path = self.get_check_dir_path()
        # Make a new directory for current check
        os.mkdir(check_dir_path)

        # Clone all github repositories and append the clone directory in 'directories' list
        # for submission in self.get_all_submissions(check_id):
        for submission in self.submissions:
            submission_dir = os.path.join(
                check_dir_path, '{}_{}'.format(submission.id, submission.name))
            os.mkdir(submission_dir)
            if len(submission.github_url) == 0:
                continue
            logger.error(f"\nCloning URL {submission.github_url}")

            try:
                repo = git.Repo.clone_from(
                    submission.github_url.strip(), submission_dir)
                if repo:
                    directories.append(submission_dir)
            except (Exception):
                logger.exception(">>> Git Error!")
                logger.debug(f"Unable to clone{submission.github_url}")
        return directories

    # Removes the check directory along with its sub directories
    # This will not remove directories in windows env because of permission issues
    def remove_submissions(self):
        check_dir_path = self.get_check_dir_path()
        shutil.rmtree(check_dir_path, ignore_errors=True)

    def run_check(self, language, directories):
        logger.error("\nInside run_check")
        # Load moss user id from env variables
        moss_user_id = os.getenv('MOSS_USER_ID')
        # Initialize Moss
        moss = mosspy.Moss(moss_user_id, language)

        if directories:
            moss.setDirectoryMode(1)
            file_exts = get_file_extensions(language)

            # Move files from subdirectories to parent directories and relevant language files
            for directory in directories:
                extract_files_from_dir(directory, self.paths)
                for ext in file_exts:
                    moss.addFilesByWildcard(directory + '/*.{}'.format(ext))
        else:
            return
        # Run Check
        url = moss.send()

        return url

    #This will send an email every run indicating about maximun jumps(percenatge increased in this run when compared to previous run) for the current run.
    def send_email(self, jumps, check_id):
        #reading the required variables to send email from .env file
        sender_email = os.getenv('SENDER_EMAIL')
        receiver_email = os.getenv('RECEIVER_EMAIL')
        password = os.getenv('APP_PASSWORD')

        #initialising to, from and subject for the email
        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Github Plagiarism Detector - Check " + str(check_id)
        text = ""
        #Email format when there is a previous run to compare
        # creating  table header and brief info about each columns 
        if jumps:
            html = """\
                    <html>
                        <head>
                            <style> 
                                table, th, td {
                                    border: 1px solid white;
                                    border-collapse: collapse;
                                }
                                th, td {
                                    background-color: #96D4D4;
                                }
                                .alnright { text-align: right; }
                                .center {
                                    margin-left: auto;
                                    margin-right: auto;
                                }
                            </style>
                        </head>
                        <body>
                            <div>
                                <div>
                                    <p><b>Below table indicates the top jumps for this check </b> </p>
                                    <p><b>NOTE:</b></p>
                                    <p><b>Repo A and Repo B :</b> These two columns indicate the team names whose code is being checked.</p>
                                    <p><b>Shared Code Repo A to B :</b> This column indicates percentage of first team A’s code that is shared with second team B for the current run.</p>
                                    <p><b>Similarity Jump Repo A to B:</b> This column indicates the difference between the similarity percentage of Team A with Team B from current run to previous run.</p>
                                    <p><b>Shared Code Repo B to A :</b> This column indicates percentage of first team B’s code that is shared with second team A for the current run.</p>
                                    <p><b>Similarity Jump Repo B to A:</b> This column indicates the difference between the similarity percentage of Team B with Team A from current run to previous run.</p>
                                </div>
                                <div>
                                    <table class="center">
                                        <tr>
                                            <th>Repo A</th>
                                            <th>Repo B</th>
                                            <th>Shared Code Repo A to B</th>
                                            <th>Shared Code Repo A to B</th>
                                            <th>Similarity Jump Repo A to B</th>
                                            <th>Similarity Jump Repo B to A</th>
                                        </tr>
                    """
            #creating table rows which will have jump info.
            for x in jumps:
                html += "<tr><td class='alnright'>" + str(x[0]) + "</td><td class='alnright'>" + str(x[1])+"%" + "</td><td class='alnright'>" + str(x[2])+"%" + "</td><td class='alnright'>" + str(x[3]) + "</td><td class='alnright'>" + str(x[4]) +"%"+ "</td><td class='alnright'>" + str(x[5]) +"%" + "</td></tr>"

            html += """\
                                    </table>
                                </div>
                            </div>
                        </body> 
                    </html>
                """
        #Email format when there is no previous run 
        else:
            html = """\
                <html>
                    <body>
                        <div>
                            <p> This is the first run. Hence can not report a change in similarity. </p>
                        </div>
                    </body>
                </html>
                """
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
