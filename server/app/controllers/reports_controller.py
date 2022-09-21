from app import db
from app.models.report import Report
from sqlalchemy import text

# Shows all of the MoSS runs on the assignment
class ReportsController:

    @staticmethod
    def new(check_id, check_date, report_link):
        report = Report(check_id, check_date, False, report_link)
        db.session.add(report)
        db.session.commit()
        return report

    def show_reports(parameters):
        """returns a list of all MOSS run of an assignment """
        check_id = parameters.get('check_id')
        result_list = []

        # For a particular check ID, arrange all the runs in descending order.
        results = Report.query.filter_by(check_id=check_id).order_by(text("reports_id desc"))
        for res in results:
            result_list.append({
                    'reportId': res.id,
                    'date': res.check_date,
                    'status': res.status,
                    'report': res.report_link
                })
        return result_list
