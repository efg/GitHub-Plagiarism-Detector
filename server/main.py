import time

from app import app
# from config import Config

# app = get_app(Config)

from app import routes

if __name__ == '__main__':
    
    app.debug = True
    app.run(debug=True)
