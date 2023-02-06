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
    return render_template('8-cities_by_states.html',
                           states)
    

@app.route("/states", strict_slashes=False)
def states():
    """Retrieves states in alphabetic order."""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Retrieves state ID"""
    for st in storage.all("State").values():
        if st.id == id:
            return render_template("9-states.html", state=st)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again the end of a request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)