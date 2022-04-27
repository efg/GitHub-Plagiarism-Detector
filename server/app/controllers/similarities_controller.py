from app import db
from app.models.similarities import Similarities
from app.utils.emailer import email_jump_info
from flask import jsonify
import os

# Extract and store all the information from the MOSS report for each run 
class SimilaritiesController:
    @staticmethod
    def new(check_id: int, report_id: int, data: list):
        maxjump =  int(os.getenv('MAXIMUM_JUMP_PERCENTAGE'))
        #initialse jumps list
        #jumps is a list of highest percentage increase in similarities in current run when compared to previous run
        jumps = []
        print(data)
        for row in data:
            first_team_info, second_team_info = row
            team1, score1 = first_team_info
            team2, score2 = second_team_info
            if not Similarities.query.filter_by(check_id=check_id,
                                                report_id=report_id,
                                                repo1=team1,
                                                repo2=team2).first():

                #Find previous run within the same check ID and for the same set of teams.
                prevRun = Similarities.query.filter_by(check_id=check_id, repo1=team1, repo2=team2, report_id=int(report_id)-1).all()

                # Calculate jump by finding the increase between current similarity score and previous run's similarity score.
                if prevRun:
                    jump1 = score1 - prevRun[0].dupl_code1
                    jump2 = score2 - prevRun[0].dupl_code2

                    #If the jump is greater than the maximum permissible jump specified by the .env file, then append it to the jumps list.
                    if jump1 >= maxjump or jump2 >= maxjump:
                        jumps.append([team1,team2 ,score1, score2, jump1, jump2])
                similar = Similarities(
                    check_id, report_id, team1, score1, team2, score2)
                db.session.add(similar)
                db.session.commit()
            else:
                print(f"\n{team1}, {team2}  data exists!")
        print("\nInside SimilaritiesController data added")
        #send email to the instructor about highest jumps after this run
        email_jump_info(jumps,check_id)

    @staticmethod
    def fetch_all_report_info(parameters):
        """returns all info scraped from the MOSS report for given check_id """
        check_id = parameters.get('check_id')
        print('\ninside fetch MOSS infos', check_id)

        MOSS_info = {}
        similarities_obj_list = Similarities.query.filter_by(
            check_id=check_id).all()

        for obj in similarities_obj_list:

            # Finding previous run within the same check ID and for the same set of teams.
            similarities_obj_list_prev = Similarities.query.filter_by(check_id=check_id, repo1=obj.repo1,
                                                                      repo2=obj.repo2, report_id=int(obj.report_id)-1).all()

            # If a previous run exists, then we calculate the similarity jump.
            if similarities_obj_list_prev:

                # We are appending information about a run such as the ID, repos being compared, similarity percentage
                # between repo A to B and vice versa and the similarity jump from previous to current run.
                if str(obj.report_id) in MOSS_info:
                    MOSS_info[str(obj.report_id)] += [{
                        'report_id': obj.report_id,
                        'repo1': obj.repo1,
                        'dupl_code1': obj.dupl_code1,
                        'repo2': obj.repo2,
                        'dupl_code2': obj.dupl_code2,
                        'similarity_jump1': obj.dupl_code1 - similarities_obj_list_prev[0].dupl_code1,
                        'similarity_jump2': obj.dupl_code2 - similarities_obj_list_prev[0].dupl_code2
                    }]

                else:
                    MOSS_info[str(obj.report_id)] = [
                        {
                            'report_id': obj.report_id,
                            'repo1': obj.repo1,
                            'dupl_code1': obj.dupl_code1,
                            'repo2': obj.repo2,
                            'dupl_code2': obj.dupl_code2,
                            'similarity_jump1': obj.dupl_code1 - similarities_obj_list_prev[0].dupl_code1,
                            'similarity_jump2': obj.dupl_code2 - similarities_obj_list_prev[0].dupl_code2
                        }
                    ]

            # If a previous run does not exist, then we update the similarity jump column to N/A.
            else:
                if str(obj.report_id) in MOSS_info:
                    MOSS_info[str(obj.report_id)] += [{
                        'report_id': obj.report_id,
                        'repo1': obj.repo1,
                        'dupl_code1': obj.dupl_code1,
                        'repo2': obj.repo2,
                        'dupl_code2': obj.dupl_code2,
                        'similarity_jump1': 'N/A',
                        'similarity_jump2': 'N/A'
                    }]
                else:
                    MOSS_info[str(obj.report_id)] = [
                        {
                            'report_id': obj.report_id,
                            'repo1': obj.repo1,
                            'dupl_code1': obj.dupl_code1,
                            'repo2': obj.repo2,
                            'dupl_code2': obj.dupl_code2,
                            'similarity_jump1': 'N/A',
                            'similarity_jump2': 'N/A'
                        }
                    ]

        # print(MOSS_info)
        return MOSS_info
