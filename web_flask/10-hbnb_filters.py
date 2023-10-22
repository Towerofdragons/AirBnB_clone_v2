#!/usr/bin/python3
"""
Script to start a flask application and listen on port 5000
and configure the route /hbnb_filters to be
rendered with template that uses data fetched from the backend
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Rendering various objects fetched from backend
    """
    from models import storage
    from models.base_model import BaseModel
    from models.state import State
    from models.city import City
    from models.amenity import Amenity

    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def tearDown(self):
    """
    Method to remove the current session
    """
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
