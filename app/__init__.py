from flask import Flask
from jinja2 import PackageLoader, PrefixLoader

app = Flask(__name__)

app.jinja_loader = PrefixLoader({
    'govuk_frontend_jinja': PackageLoader('govuk_frontend_jinja', '.'),
    'app': PackageLoader('app'),
})

from app import routes
