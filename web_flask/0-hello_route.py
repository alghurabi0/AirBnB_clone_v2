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
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
