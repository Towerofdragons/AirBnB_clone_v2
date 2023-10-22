#!/usr/bin/python3
"""
Script to start a flask application and listen on port 5000
and configure the route /states and /states/<id> to be 
rendered with template that uses data fetched from the backend
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Rendering state object fetched from backend
    """
    from models import storage
    from models.base_model import BaseModel
    from models.state import State

    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """
    Rendering html template with state and its cities data
    retrieved from the backend
    """
    from models import storage
    from models.base_model import BaseModel
    from models.state import State
    from models.city import City
    states = storage.all(State).values()
    state = next((state for state in states if state.id == id), None)
    if state is not None:
        all_cities = storage.all(City).values()
        cities = [city for city in all_cities if city.state_id == state.id]
        return render_template('9-states.html', state=state,
                           cities=cities)
    else:
        return render_template('9-states.html')


@app.teardown_appcontext
def tearDown(self):
    """
    Method to remove the current session
    """
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
