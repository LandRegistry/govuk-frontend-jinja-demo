from flask import Flask
from flask_compress import Compress
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__, static_url_path="/assets")

app.jinja_loader = ChoiceLoader(
    [
        PackageLoader("app"),
        PrefixLoader({"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}),
    ]
)

Compress(app)

from app import routes
