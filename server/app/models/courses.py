from app import db

class Course(db.Model):
    __tablename__ = 'courses'

    # Columns for course table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    active = db.Column(db.Boolean)
    users = db.relationship('User', backref='courses')

    def __init__(self, name, active=True):
        self.name = name
        self.active = active
    
    
