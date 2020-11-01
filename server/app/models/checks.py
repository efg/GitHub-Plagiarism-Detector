from app import db
from app.utils.languages import get_file_extensions
from app.utils.directories import move_to_root_folder
import mosspy
import os
from dotenv import load_dotenv
load_dotenv()

class Check(db.Model):
    __tablename__ = 'checks'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id", ondelete='CASCADE'), nullable = False)
    name = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    # Time interval after which to run the check again
    interval = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, nullable = False)

    def __init__(self, name, course_id, start_date, end_date, interval, is_active = True):
        self.name = name
        self.course_id = course_id
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.is_active = is_active
    
    def run_check(self, language, directories=[], files=[]):
        # Load moss user id from env variables
        moss_user_id = os.getenv('MOSS_USER_ID')
        # Initialize Moss
        moss = mosspy.Moss(moss_user_id, language)

        if directories:
            moss.setDirectoryMode(1)
            file_exts = get_file_extensions(language)
            
            # Move files from subdirectories to parent directories and relevant language files
            for directory in directories:
                move_to_root_folder(directory, directory)
                for ext in file_exts:
                    moss.addFilesByWildcard(directory + '*.{}'.format(ext))
        else:
            for file in files:
                moss.addFile(file)
        # Run Check
        url = moss.send()
        return url





