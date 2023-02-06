#!/usr/bin/python3
"""State module"""
from flask import Flask, render_template
from models import storage
from os import getenv
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Retrieves state information."""
    return render_template('7-states_list.html',
                           s=[i for i in storage.all('State').values()])


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """Retrieves cities by states."""
    s = storage.all('state')
    states=[i for i in s.values()]


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again the end of a request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)