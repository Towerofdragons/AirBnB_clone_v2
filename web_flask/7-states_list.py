#!/usr/bin/python3
"""
Script to start a flask application and listen on port 5000
and configure the route /states_list to be rendered with template
that uses data fetched from the backend
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    Rendering html template and displaying data retrieved
    from the backend
    """
    from models import storage
    from models.base_model import BaseModel
    from models.state import State
    states = storage.all(State)
    print(states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearDown(self):
    """
    Method to remove the current session
    """
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
