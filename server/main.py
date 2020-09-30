from flask import redirect, url_for
from app import get_app
from config import Config

app = get_app(Config)

from app import routes

if __name__ == '__main__':
    app.run()