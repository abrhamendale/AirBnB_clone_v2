#!/usr/bin/python3
"""
Hello route module.
"""
from flask import Flask
hello = Flask(__name__)

@hello.route('/', strict_slashes=False)
def hello_route():
    return 'Hello, HBNB!'
