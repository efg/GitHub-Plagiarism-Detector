from app import db


class Similarities(db.Model):
    """Stores data from MOSS report"""
    __tablename__ = 'similarities'

    id = db.Column(db.Integer, primary_key=True)
    check_id = db.Column(db.Integer,
                         db.ForeignKey(
                             "checks.id",
                             ondelete='CASCADE'),
                         nullable=False)
    report_id = db.Column(db.Integer,
                          db.ForeignKey(
                              "reports.id",
                              ondelete='CASCADE'),
                          nullable=False)
    team1 = db.Column(db.String(50), nullable=False)
    team2 = db.Column(db.String(50), nullable=False)
    score1 = db.Integer(db.Float(4, 2), nullable=False)
    score2 = db.Integer(db.Float(4, 2), nullable=False)
    change = db.Integer(db.Float(4, 2), nullable=False)

    def __init__(self,
                 check_id,
                 report_id,
                 team1,
                 team2,
                 score1,
                 score2,
                 change):
        self.check_id = check_id
        self.report_id = report_id
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2
        self.change = change
