from app import db
from app.models.reports import Report

class ReportsController:

    @staticmethod
    def new(check_id, check_date, report_link):
        
        report = Report(check_id, check_date, False, report_link)
        db.session.add(report)
        db.session.commit()
        return report

    def show_reports(parameters):
        check_id = parameters.get('check_id')
        result_list = []
        results = Report.query.filter_by(check_id = check_id)
        for res in results:
            result_list.append(
                    {'date': res.check_date, 
                    'status': res.status, 
                    'report': res.report_link})
        return result_list