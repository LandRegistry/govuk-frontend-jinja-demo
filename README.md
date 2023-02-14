# GOV.UK Frontend Jinja Demo

Demo Flask app using [GOV.UK Frontend Jinja](https://github.com/LandRegistry/govuk-frontend-jinja) macros.

> **IMPORTANT**: This app is deprecated. It is only meant to demonstate all of the `govuk-frontend-jinja` component macros. It is not meant to be used as the basis for a full Flask app. If you are looking to build a fully featured Flask app that integrates with [GOV.UK Frontend Jinja](https://github.com/LandRegistry/govuk-frontend-jinja) and [GOV.UK Frontend WTForms](https://github.com/LandRegistry/govuk-frontend-wtf) please use the [GOV.UK Frontend Flask](https://github.com/LandRegistry/govuk-frontend-flask) template to [generate your app](https://github.com/LandRegistry/govuk-frontend-flask/generate) instead.

## Getting started

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt ; pip3 install -r requirements_dev.txt
./build.sh
flask run
```
