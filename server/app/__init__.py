from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS
import time
 
# Initialize SQLAlchemy instance to communicate with the database 
db = SQLAlchemy()
app = None
scheduler = BackgroundScheduler(daemon=True)

def get_app(Config=None):
    global app
    if app:
        return app

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    db.app = app
    Migrate(app,db)
    scheduler.start()
    
    from app.models import users, courses, submissions, checks, paths

    return app
