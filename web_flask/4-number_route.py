#!/usr/bin/python3
"""
Script to start a flask application and listen on port 5000
and configure the route /number/<n>
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Displaying a text in the home route
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Configuring a new route /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Configuring a new route using user input """
    return "C " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ Defining a /python/<text> route via default text"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Displaying number only if it is an integer """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
