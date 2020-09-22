from flask import redirect, url_for
from app import create_app
from config import Config

app = create_app(Config)

@app.route('/index', methods=['get', 'post'])
def index():
    return '<br>&nbspHello World, Flask lives.'

@app.route('/', methods=['get', 'post'])
def landing():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()