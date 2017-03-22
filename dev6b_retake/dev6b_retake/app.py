"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, url_for
from controller import *
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    return Controller.index()

@app.route('/a1', methods=['GET', 'POST'])
def a1():
    return Controller.a1()

@app.route('/a2', methods=['GET', 'POST'])
def a2():
    return Controller.a2()

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
