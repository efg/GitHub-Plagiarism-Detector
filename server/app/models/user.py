from app import db
from app.models.course import Course

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, index = True, unique=True)
    password = db.Column(db.String(128), nullable=False)

    # Whether this user is the admin
    admin = db.Column(db.Boolean)
    
    def __init__(self, name, email, password, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
    
