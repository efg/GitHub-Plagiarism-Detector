from flask import Flask, jsonify, make_response, request, redirect, url_for


app = Flask(__name__)

@app.route('/index', methods=['get', 'post'])
def index():
    return '<br>&nbspHello World, Flask lives.'

@app.route('/', methods=['get', 'post'])
def landing():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()