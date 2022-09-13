#!/usr/bin/python3
"""Python Script that starts a Flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Allows the root route '/' to return text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index_01():
    """Allows the route '/hbnb' to return text""""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def index_02(text):
    """Allows the route '/c/' to return given text inside the page"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index_03(text='is cool'):
    """Allows the route '/python/' to return given text inside the page"""
    return 'Python ' + text.replace('_', ' ')


@procFlask.route('/number/<int:n>', strict_slashes=False)
def index_04(n):
    """Allows the route '/number/' to return given integer inside the page"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
