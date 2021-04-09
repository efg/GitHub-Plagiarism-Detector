from app import db
from app.models.similarities import Similarities

class ScrapeController:
    @staticmethod
    def new(check_id: int, report_id: int, data: list):
        print(data)
        for row in data:
            first_team_info, second_team_info = row 
            team1, score1 = first_team_info
            team2, score2 = second_team_info 
            if not Similarities.query.filter_by(check_id=check_id, 
                report_id=report_id,
                first=team1,
                second=team2).first():
                similar = Similarities(report_id, report_id, team1, score1, team2, score2)  
                db.session.add(similar)
                db.session.commit()
                print("\ninside Scrapecontroller", "data added")
            else:
                print(f"\n{team1}, {team2}  data exists!")