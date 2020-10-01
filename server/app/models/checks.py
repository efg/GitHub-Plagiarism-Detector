from app import db

class Check(db.Model):
    __tablename__ = 'checks'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id", ondelete='CASCADE'), nullable = False)
    name = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    # Time interval after which to run the check again
    interval = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, nullable = False)
    

    def __init__(self, name, course_id, start_date, end_date, interval, is_active = True):
        self.name = name
        self.course_id = course_id
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.is_active = is_active
