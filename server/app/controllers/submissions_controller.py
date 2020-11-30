from app import db
from app.models.submissions import Submission
from app.utils.csv_parser import parse
from app.models.checks import Check

class SubmissionController:
    
    # Adds new entries to submission controller and returns duplicate entries if found any.
    # TODO: Handle return values in front-end
    # Parameters should have fields named header(for csv files), check_id
    @staticmethod
    def new(parameters, param_file):

        duplicate_entries = []
        check_id = parameters['check_id']
        csv_entries = parse(param_file,parameters['header'])        # csv_entries = [[team_name, github_url]]

        # Iterate over submission_ids
        for i, entry in enumerate(csv_entries):
            curr_team = entry[0]
            curr_url = entry[1]
            if not Submission.query.filter_by(check_id=check_id, name=curr_team, github_url=curr_url).first():
                # Create a new entry for submission table and save to db
                submission = Submission(curr_team, check_id, curr_url)
                db.session.add(submission)
                db.session.commit()
            else: 
                # Duplicate submission details are added to a list to display on the page
                duplicate_entries.append([curr_team, curr_url])

        return duplicate_entries

    @staticmethod
    def list_submissions(parameters):

        list_of_submissions = []
        
        for submission in Check.query.filter_by(id=parameters['check_id']).first().submissions:
            list_of_submissions.append({'name': submission.name, 'github_url': submission.github_url})
        
        return list_of_submissions