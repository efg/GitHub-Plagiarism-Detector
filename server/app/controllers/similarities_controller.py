from app import db
from app.models.similarities import Similarities

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
                similar = Similarities(check_id, report_id, team1, score1, team2, score2)  
                db.session.add(similar)
                db.session.commit()
            else:
                print(f"\n{team1}, {team2}  data exists!")
        print("\nInside SimilaritiesController data added")