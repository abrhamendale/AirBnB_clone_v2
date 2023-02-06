#!/usr/bin/python3
"""Hello route module."""


from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Hello route function"""
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Hello hbnb function"""
    return 'HBNB'


@app.route('/c/<user>', strict_slashes=False)
def hello_c(user):
    """Hello c function"""
    return 'C %s' % user.replace("_", " ")


@app.route('/python', defaults={'user': 'is cool'})
@app.route('/python/<user>')
def hello_py(user):
    """Python function"""
    return 'Python {}'.format(user.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Outputs integers"""
    return '{:d} is a number'.format(n)


if __name__ == "__main__":
    """Main function"""
    app.run(host="0.0.0.0", port=5000)