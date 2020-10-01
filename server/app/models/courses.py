from app import db

class Course(db.Model):
    __tablename__ = 'courses'

    # Columns for course table
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable = False, index = True)
    name = db.Column(db.String(64))
    active = db.Column(db.Boolean)

    def __init__(self, user_id, name, active=True):
        self.user_id = user_id
        self.name = name
        self.active = active
    
    
