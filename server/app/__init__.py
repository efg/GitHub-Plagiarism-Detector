from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy instance to communicate with the database 
db = SQLAlchemy()
app = None

def get_app(Config=None):
    global app
    if app:
        return app

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app,db)

    from app.models import users, courses, submissions, checks, paths

    return app
