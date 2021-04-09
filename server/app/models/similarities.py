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
                         nullable=False)
    report_id = db.Column(db.Integer,
                         db.ForeignKey(
                             "reports.id",
                             ondelete='CASCADE'),
                         nullable=False)

    repo1 = db.Column(db.String(100), nullable=False)
    dupl_code1 = db.Column(db.Float, nullable=False)
    
    repo2 = db.Column(db.String(100), nullable=False)
    dupl_code2 = db.Column(db.Float, nullable=False)
        
    

    def __init__(self, check_id, report_id, repo1, dupl_code1, repo2, dupl_code2):
        self.check_id = check_id
        self.report_id = report_id
        self.repo1 = repo1
        self.dupl_code1 = dupl_code1
        self.repo2 = repo2
        self.dupl_code2 = dupl_code2
        
        
