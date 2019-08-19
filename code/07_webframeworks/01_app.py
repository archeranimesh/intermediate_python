# MAC 
# FLASK_APP=01_app.py flask run
# Reload the flask app on save.
# FLASK_APP=01_app.py FLASK_ENV=development flask run

# Windows
# $env:FLASK_APP = "01_app.py"; flask run
# $env:FLASK_APP = "01_app.py"; $env:FLASK_ENV = "development"; flask run
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/french")
def bounjour_world():
    return "Bonjour, World!"

# Paramater routing.
@app.route("/name/<name>")
def how_world(name):
    return f"hello! {name}"