from app import db


class Similarities(db.Model):
    """
    Stores all necessary information from MOSS report 
    including team name, code similarity score
    """
    __tablename__ = 'similarities'

    id = db.Column(db.Integer, primary_key=True)
    check_id = db.Column(db.Integer,
                         db.ForeignKey(
                             "checks.id",
                             ondelete='CASCADE'),
                         nullable=False),
    report_id = db.Column(db.Integer,
                         db.ForeignKey(
                             "reports.id",
                             ondelete='CASCADE'),
                         nullable=False),
    
    
    first = db.Column(db.String(100), nullable=False)
    first_match_score = db.Column(db.Float, nullable=False)
    
    second = db.Column(db.String(100), nullable=False)
    second_match_score = db.Column(db.Float, nullable=False)
        
    

    def __init__(self, check_id, report_id, first, first_match_score, second, second_match_score):
        self.check_id = check_id
        self.report_id = report_id,
        self.first = first,
        self.first_match_score = first_match_score,
        self.second = second,
        self.second_match_score = second_match_score,
        
        
