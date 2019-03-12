from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    print(request.method)
    print(request.headers)
    return '<h1>Learning Flask</h1>'


@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}'
