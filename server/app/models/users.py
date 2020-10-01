from app import db
from app.models.courses import Course

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id", ondelete='CASCADE'), nullable = False)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, index = True, unique=True)
    password = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean)
    
    def __init__(self, course_id, name, email, password, admin=False):
        self.course_id = course_id
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
    
