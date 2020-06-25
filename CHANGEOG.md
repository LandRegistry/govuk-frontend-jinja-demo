# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/matthew-shaw/govuk-frontend-jinja-example/compare/0.3.0...master)

## [0.3.0](https://github.com/matthew-shaw/govuk-frontend-jinja-example/releases/tag/0.3.0) - 25/06/2020

### Added

- Script to pull down [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend/) to the app's `static` directory
- Set asset paths to get static CSS, JS and image content
- `Procfile` and `gunicorn` requirements to deploy to Heroku

## [0.2.0](https://github.com/matthew-shaw/govuk-frontend-jinja-example/releases/tag/0.2.0) - 18/06/2020

### Changed

- Updated to use `govuk-frontend-jinja` [release 0.2.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.2.0)
- Changed Jinja loader to `ChoiceLoader` to access templates without a namespace prefix
- Removed `app/*` prefix from template
- Changed `index.html` template to extend base [GOV.UK page template](https://design-system.service.gov.uk/styles/page-template/)

## [0.1.0](https://github.com/matthew-shaw/govuk-frontend-jinja-example/releases/tag/0.1.0) - 12/06/2020

### Added

- Very basic [Flask](https://flask.palletsprojects.com/) app to demonstrate using the `govuk-frontend-jinja` package [release 0.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.1.0).
