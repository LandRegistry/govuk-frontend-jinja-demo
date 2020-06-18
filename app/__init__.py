from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)

loader = ChoiceLoader([
    PackageLoader('app'),
    PrefixLoader({
        'govuk_frontend_jinja': PackageLoader('govuk_frontend_jinja')
    })
])
app.jinja_loader = loader

from app import routes
