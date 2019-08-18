# MAC 
# FLASK_APP=01_app.py flask run

# Windows
# $env:FLASK_APP = "01_app.py"; flask run
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"