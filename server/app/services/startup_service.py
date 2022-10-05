from datetime import datetime
from tabnanny import check
from app.models.check import Check
from app.controllers.checks_controller import ChecksController

from app import scheduler

class StartUpService:

    @staticmethod
    def schedule_jobs():
        check_entries = Check.query.filter_by(is_active=True, visibility="yes")
        for entry in check_entries:
            start_date = entry.start_date
            end_date = entry.end_date

            today = datetime.now()

            if(today > end_date and today < start_date):
                continue

            scheduler.add_job(
                func=ChecksController.run,
                trigger="interval",
                minutes=5,
                args=[entry.id],
                next_run_time=datetime.now())

            

