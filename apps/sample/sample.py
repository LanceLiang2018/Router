from flask import *


app = Flask('sample')


@app.route('/')
def index():
    return 'This is a sample app'


if __name__ == '__main__':
    app.run('0.0.0.0', port=8001, debug=False)
