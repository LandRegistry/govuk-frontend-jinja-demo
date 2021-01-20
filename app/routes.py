import json

from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/components")
def components():
    return render_template("components.html")


@app.route("/components/<string:component>")
def component(component):
    with open("govuk_components/{}/fixtures.json".format(component)) as json_file:
        fixtures = json.load(json_file)

    return render_template("component.html", fixtures=fixtures)
