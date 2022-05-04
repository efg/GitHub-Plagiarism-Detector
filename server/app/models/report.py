from app import db
import os
from app.models.similarity import Similarities
from app.utils.emailer import email_jump_info


class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    check_id = db.Column(db.Integer, db.ForeignKey(
        "checks.id", ondelete='CASCADE'), nullable=False)
    check_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    report_link = db.Column(db.String(100), nullable=False)

    def __init__(self, check_id, check_date, status, report_link):
        self.check_id = check_id
        self.check_date = check_date
        self.report_link = report_link
        self.status = status
        
    #This function calculates and send email to the instructor about highest jumps after this run
    def calculateJumps(self,check_id,report_id,data):
        jumps = []
        for row in data:
            maxjump =  int(os.getenv('MAXIMUM_JUMP_PERCENTAGE'))
            #initialse jumps list
            #jumps is a list of highest percentage increase in similarities in current run when compared to previous run
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

                    #If the jump is greater than the minimum jump specified in the .env file, then append it to an jumps list.
                    if jump1 >= maxjump or jump2 >= maxjump:
                        jumps.append([team1,team2 ,score1, score2, jump1, jump2])
        
        #send email to the instructor about highest jumps after this run
        email_jump_info(jumps,check_id)
        
