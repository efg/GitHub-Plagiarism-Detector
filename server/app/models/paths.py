from app import db


class Path(db.Model):
    __tablename__ = 'paths'

    id = db.Column(db.Integer, primary_key=True)
    check_id = db.Column(db.Integer, db.ForeignKey(
        "checks.id", ondelete='CASCADE'), nullable=False)
    path = db.Column(db.String(256), nullable=False)

    def __init__(self, check_id, path):
        self.check_id = check_id
        self.path = path
