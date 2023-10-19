#!/usr/bin/python3
"""
Script to start a flask application and listen on port 5000.
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Displaying a text in the home route
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
