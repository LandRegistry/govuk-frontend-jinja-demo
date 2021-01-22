import json
import os

from flask import render_template

from app import app


@app.route("/")
def index():
    components = os.listdir("govuk_components")
    components.sort()

    return render_template("index.html", components=components)


@app.route("/components/<string:component>")
def component(component):
    with open("govuk_components/{}/fixtures.json".format(component)) as json_file:
        fixtures = json.load(json_file)

    return render_template("component.html", fixtures=fixtures)
