from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__, static_url_path='/assets')

app.jinja_loader = ChoiceLoader([
    PackageLoader('app'),
    PrefixLoader({
        'govuk_frontend_jinja': PackageLoader('govuk_frontend_jinja')
    })
])

from app import routes
