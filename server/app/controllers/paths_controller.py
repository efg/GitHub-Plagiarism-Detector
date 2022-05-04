from app import db
from app.models.path import Path
from app.utils.csv_parser import parse

# The relative paths for the files to include in the MOSS check 
class PathsController:

    @staticmethod
    def new(parameters, csv_file):
        print(csv_file)
        paths = parse(csv_file, parameters['header'])
        for path in paths:
            new_path = Path(parameters['check_id'], path)
            db.session.add(new_path)
            db.session.commit()
