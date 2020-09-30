from app import get_app

app = get_app()

@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    return '<br>&nbspHello World, Flask lives.'