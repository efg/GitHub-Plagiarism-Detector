from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route('/index', methods=['get', 'post'])
def index():
    return '<br>&nbspHello World, Flask lives.'


if __name__ == '__main__':
    app.run()