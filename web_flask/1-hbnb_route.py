#!/usr/bin/python3
"""
Script to start a flask application and listen on port 5000
and configure the route /hbnb
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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
