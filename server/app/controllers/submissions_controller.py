from app import db
from app.models.submissions import Submission
from app.utils.csv_parser import parse
from app.models.checks import Check
from app.models.paths import Path

# Read and store all the infomation from user input as well as CSV files then 
# clone all repos to run MOSS later
class SubmissionController:

    # Adds new entries to submission controller and returns duplicate entries if found any.
    # Parameters should have fields named header(for csv files), check_id
    @staticmethod
    def new(parameters, param_files):
        
        check_id = parameters['check_id']

        for csv_name, csv_obj in param_files.to_dict().items():
            csv_entries = parse(csv_obj, parameters['header'])
            
            if csv_name == "csvFile":
                for curr_team, curr_url  in csv_entries:
                    if not Submission.query.filter_by(check_id=check_id,
                                                    name=curr_team,
                                                    github_url=curr_url).first():
                        # Create a new entry for submission table and save to db
                        submission = Submission(curr_team, check_id, curr_url)
                        db.session.add(submission)
                        db.session.commit()
            elif csv_name == "pathscsv":
                for entry in csv_entries:
                    if not Path.query.filter_by(check_id=check_id, 
                                                path=entry[0]).first():
                        # Create a new entry for paths table and save to db
                        path = Path(check_id, entry[0])
                        db.session.add(path)
                        db.session.commit()
            else:
                raise ValueError("\n>>>Invalid FileName!!!\n")

    @staticmethod
    def list_submissions(parameters):

        list_of_submissions = []

        for submission in Check.query.filter_by(id=parameters['check_id']).first().submissions:
            list_of_submissions.append(
                {'name': submission.name, 'github_url': submission.github_url})

        return list_of_submissions
