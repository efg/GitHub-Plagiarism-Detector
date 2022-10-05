from flask import redirect, url_for
from app import get_app
from config import Config
from app.services.startup_service import StartUpService

app = get_app(Config)

from app import routes

if __name__ == '__main__':
    StartUpService.schedule_jobs()
    app.run()
    
