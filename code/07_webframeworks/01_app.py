# MAC 
# FLASK_APP=01_app.py flask run
# Reload the flask app on save.
# FLASK_APP=01_app.py FLASK_ENV=development flask run

# Windows
# $env:FLASK_APP = "01_app.py"; flask run
# $env:FLASK_APP = "01_app.py"; $env:FLASK_ENV = "development"; flask run
from flask import Flask
# this is for working with templates.
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # no need to give the templates directory
    name = "XYZ"
    return render_template("index.html", name=name)

@app.route("/french")
def bounjour_world():
    return "Bonjour, World!"

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# Paramater routing.
@app.route("/name/<name>")
def how_world(name):
    return f"hello! {name}"