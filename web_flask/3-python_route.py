#!/usr/bin/python3
"""This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
Routes:
/: display "Hello HBNB!"
You must use the option strict_slashes=False in your route definition.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Show 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Show 'C' then text var"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """Show 'Python' then text var"""
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
