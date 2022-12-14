from datetime import datetime, timedelta
from tabnanny import check
from app.models.check import Check
from app.controllers.checks_controller import ChecksController

from app import scheduler

class StartUpService:

    # This method schedules all the active jobs to the scheduler during startup.
    # It loops over all the checks, and only schedules jobs whose end_date is after the 
    # current date.
    @staticmethod
    def schedule_jobs():
        check_entries = Check.query.filter_by(is_active=True, visibility="yes")
        for entry in check_entries:
            start_date = entry.start_date
            end_date = entry.end_date

            today = datetime.now()

            if(today > end_date and today < start_date):
                continue
            
            ChecksController.schedule_job(datetime.now(), end_date, entry.id,)

            

