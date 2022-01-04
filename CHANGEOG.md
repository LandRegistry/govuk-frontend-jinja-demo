# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/LandRegistry/govuk-frontend-jinja-demo/compare/2.0.0...main)

## [2.0.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/2.0.0) - 14/10/2021

### Added

- [GOV.UK Frontend v4.0.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.0.0) support

### Changed

- Updated `govuk-frontend-jinja` to [release 2.0.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.0.0)

### Removed

- Python 3.6 support

## [1.8.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.8.0) - 14/10/2021

### Added

- Support for [Python v3.10](https://www.python.org/downloads/release/python-3100/)

### Changed

- Updated `govuk-frontend-jinja` to [release 1.5.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.5.1)
- Updated `govuk-frontend` to [release 3.14.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.14.0)
- Updated `flask` to [release v2.0.2](https://flask.palletsprojects.com/en/2.0.x/changes/)
- Updated `jinja2` to [release v3.0.2](https://jinja.palletsprojects.com/en/3.0.x/changes/)
- Updated Python runtime to 3.9.7

## [1.7.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.7.0) - 29/06/2021

### Changed

- Updated `govuk-frontend-jinja` to [release 1.4.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.4.0)
- Updated `govuk-frontend` to [release 3.13.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.13.0)

## [1.6.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.6.0) - 21/05/2021

### Changed

- Updated `govuk-frontend-jinja` to [release 1.3.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.3.0)
- Updated `govuk-frontend` to [release 3.12.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.12.0)

## [1.5.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.5.0) - 25/02/2021

## Added

- Link to [GOV.UK Frontend WTForms](https://govuk-frontend-wtf.herokuapp.com/) package demo.

## Fixed

- `img-src` content security policy (CSP) violation.
- Corrected heading classes

## [1.4.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.4.0) - 09/02/2021

### Changed

- Updated `govuk-frontend-jinja` to [release 1.2.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.2.0)
- Updated `govuk-frontend` to [release 3.11.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.11.0)

## [1.3.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.3.0) - 25/01/2021

### Added

- Error handlers and pages for 404 and 500 errors.
- Compressed response encoding support (gzip, brotli and deflate).
- Strict content security policy (self plus specific in-line script hashes).
- Additional security related HTTP headers implemented (strict transport security, referrer policy, XSS protection etc).
- HTML meta tags (description, keywords and author).
- Trim and strip whitespace around content blocks.

### Removed

- Duplicated skiplink block in base template

## [1.2.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.2.0) - 22/01/2021

### Added

- Using GOV.UK Frontend test fixtures to generate an index of components along with a page per component that renders every visual fixture along with its Jinja and HTML source.

### Changed

- Updated index page with more description about what this app is for.
- Put links to source, build, package and demo along with credit to the package contributors, in page footer.

### Removed

- Manually created index page of component examples.

## [1.1.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.1.0) - 18/12/2020

### Added

- Text input prefix and suffix example
- Header component with navigation example
- Notification banner component examples

### Changed

- Updated `govuk-frontend-jinja` to [release 1.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.1.0)
- Updated `govuk-frontend` to [release 3.10.2](https://github.com/alphagov/govuk-frontend/releases/tag/v3.10.2)

## [1.0.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/1.0.0) - 20/08/2020

### Changed

- Updated `govuk-frontend-jinja` to [release 1.0.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.0.0)
- Updated `govuk-frontend` to [release 3.8.1](https://github.com/alphagov/govuk-frontend/releases/tag/v3.8.1)
- Changed `govukInput` macros to use new `spellcheck` option instead of the `attributes` option

## [0.3.1](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/0.3.1) - 25/06/2020

### Changed

- Update to use `govuk-frontend-jinja` [release 0.2.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.2.1)

## [0.3.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/0.3.0) - 25/06/2020

### Added

- Script to pull down [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend/) to the app's `static` directory
- Set asset paths to get static CSS, JS and image content
- `Procfile` and `gunicorn` requirements to deploy to Heroku

## [0.2.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/0.2.0) - 18/06/2020

### Changed

- Updated to use `govuk-frontend-jinja` [release 0.2.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.2.0)
- Changed Jinja loader to `ChoiceLoader` to access templates without a namespace prefix
- Removed `app/*` prefix from template
- Changed `index.html` template to extend base [GOV.UK page template](https://design-system.service.gov.uk/styles/page-template/)

## [0.1.0](https://github.com/LandRegistry/govuk-frontend-jinja-demo/releases/tag/0.1.0) - 12/06/2020

### Added

- Very basic [Flask](https://flask.palletsprojects.com/) app to demonstrate using the `govuk-frontend-jinja` package [release 0.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.1.0).
