#!/usr/bin/python3
"""
Script to start a flask application and listen on port 5000
and configure the route /c/text
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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
