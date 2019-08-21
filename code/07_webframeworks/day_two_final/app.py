"""
A Simple Flask web application interface
For viewing popular Github repos sorted by stars using the
Github search API.

To run:
MAC
(env) FLASK_APP=app.py flask run
(env) FLASK_APP=app.py FLASK_ENV=development flask run

Windows
$env:FLASK_APP = "app.py"; flask run
$env:FLASK_APP = "app.py"; $env:FLASK_ENV = "development"; flask run
"""
from flask import Flask, render_template, request
from repos.exceptions import GitHubApiError
from repos.api import repos_with_most_stars

app = Flask(__name__)

available_languages = ["Python", "JavaScript", "Ruby", "Java"]

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # Use the list of all languages.
        selected_languages = available_languages
    elif request.method == "POST":
        selected_languages = request.form.getlist("languages")

    results = repos_with_most_stars(selected_languages)

    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results
    )


@app.errorhandler(GitHubApiError)
def handle_api_error(error):
    return render_template('error.html', message=error)