from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, redirect, url_for
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance to communicate with the database

# app = None
scheduler = BackgroundScheduler(daemon=True)


# def get_app(Config=None):
    # global app
    # if app:
    #     return app

    
    # app.config.from_object(Config)
    # db.init_app(app)
    # db.app = app
    # Migrate(app, db)
    # scheduler.start()
    
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import routes
from app.models import checks, courses, paths, submissions, users

    # return app
