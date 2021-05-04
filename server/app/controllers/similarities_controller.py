from app import db
from app.models.similarities import Similarities
from flask import jsonify

# Extract and store all the information from the MOSS report for each run 
class SimilaritiesController:
    @staticmethod
    def new(check_id: int, report_id: int, data: list):
        print(data)
        for row in data:
            first_team_info, second_team_info = row
            team1, score1 = first_team_info
            team2, score2 = second_team_info
            if not Similarities.query.filter_by(check_id=check_id,
                                                report_id=report_id,
                                                repo1=team1,
                                                repo2=team2).first():
                similar = Similarities(
                    check_id, report_id, team1, score1, team2, score2)
                db.session.add(similar)
                db.session.commit()
            else:
                print(f"\n{team1}, {team2}  data exists!")
        print("\nInside SimilaritiesController data added")

    @staticmethod
    def fetch_all_report_infos(parameters):
        """returns all info scraped from the MOSS report for given check_id """
        check_id = parameters.get('check_id')
        print('\ninside fetch MOSS infos', check_id)

        MOSS_info = {}
        similarities_obj_list = Similarities.query.filter_by(
            check_id=check_id).all()

        for obj in similarities_obj_list:
            if str(obj.report_id) in MOSS_info:
                MOSS_info[str(obj.report_id)] += [{
                    'report_id': obj.report_id,
                    'repo1': obj.repo1,
                    'dupl_code1': obj.dupl_code1,
                    'repo2': obj.repo2,
                    'dupl_code2': obj.dupl_code2,
                }]
            else:
                MOSS_info[str(obj.report_id)] = [
                    {
                        'report_id': obj.report_id,
                        'repo1': obj.repo1,
                        'dupl_code1': obj.dupl_code1,
                        'repo2': obj.repo2,
                        'dupl_code2': obj.dupl_code2,
                    }
                ]
        # print(MOSS_info)
        return MOSS_info
