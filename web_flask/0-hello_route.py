#!/usr/bin/python3
"""Hello route module."""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Hello route function"""
    return 'Hello, HBNB!'


if __name__ == "__main__":
    """Main function"""
    app.run(host="0.0.0.0", port=5000)
