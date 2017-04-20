"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, url_for, render_template, json, jsonify
import mysql.connector

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/a1', methods=['GET', 'POST'])
def a1():
    return render_template('A1.html')

@app.route('/a1answers.json')
def a1answers():
    a = []
    query = "SELECT answer FROM a1;";
    db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="tommyvg")
    execute = db.cursor()
    execute.execute(query)
    answer = execute.fetchall()
    db.close()
    print(answer)
    collectionString = "answersdata=[{\n"
    first = True;
    for row in answer:

        if (first == False):
            collectionString += ",{\n"
        else:
            first = False;
        collectionString += ("\t\"answer\":\"" + str(row[0]) + "\"}\n")
    collectionString += "]"
    return collectionString

@app.route('/a2', methods=['GET', 'POST'])
def a2():
    return render_template('A2.html')

@app.route('/a2answers.json')
def a2answers():
    a = []
    query = "SELECT answer FROM a2;";
    db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="tommyvg")
    execute = db.cursor()
    execute.execute(query)
    answer = execute.fetchall()
    db.close()
    print(answer)
    collectionString = "answersdata=[{\n"
    first = True;
    for row in answer:

        if (first == False):
            collectionString += ",{\n"
        else:
            first = False;
        collectionString += ("\t\"answer\":\"" + str(row[0]) + "\"}\n")
    collectionString += "]"
    return collectionString

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
