from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(Config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app,db)

    from app.models import users

    return app
