from app import db

class Submission(db.Model):
    __tablename__ = 'submissions'

    id = db.Column(db.Integer, primary_key=True)
    check_id = db.Column(db.Integer, db.ForeignKey("checks.id", ondelete='CASCADE'), nullable = False)
    name = db.Column(db.String(64), nullable=False)
    github_url = db.Column(db.String(64), nullable=False)

    def __init__(self, name, check_id, github_url):
        self.name = name
        self.check_id = check_id
        self.github_url = github_url