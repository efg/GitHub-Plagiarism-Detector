from app import db

class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    check_id = db.Column(db.Integer, db.ForeignKey("checks.id", ondelete='CASCADE'), nullable = False)
    check_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable = False)
    report_link = db.Column(db.String(100), nullable=False)

    def __init__(self, check_id, check_date, status, report_link):
        self.check_id = check_id
        self.check_date = check_date
        self.report_link = report_link
        self.status = status