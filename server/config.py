import os
from dotenv import load_dotenv
load_dotenv()

db_server = os.getenv('DB_SERVER')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

class Config():
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(db_user, db_password, db_server, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False