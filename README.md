# Algorithms

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![hooks](https://github.com/br3ndonland/algorithms/workflows/hooks/badge.svg)
![tests](https://github.com/br3ndonland/algorithms/workflows/tests/badge.svg)

Brendon Smith ([br3ndonland](https://github.com/br3ndonland/))

## Description

This repository contains solutions to common computer science algorithm problems in Python and JavaScript. It was generated from [br3ndonland/template-python](https://github.com/br3ndonland/template-python), a useful source of default tooling for my projects.

## Directory structure

This project contains JavaScript, Python, and Terraform code. Each language is separated into its own sub-directory: _js_ for JavaScript, _py_ for Python, and _terraform_ for Terraform. The directory structure within each language's sub-directory follows the conventions for that language.

JavaScript applications typically use _src_ for source code and _tests_ for tests.

The convention in the Python community is to put application code either in _packagename_, or in _src/packagename_, with tests in _tests_. Typically the _packagename_ directory contains the source code used to build the Python package _packagename_. Some examples:

- [FastAPI](https://github.com/tiangolo/fastapi) uses _fastapi/fastapi_
- [Flask](https://github.com/pallets/flask) uses _flask/src/flask_
- [Pandas](https://github.com/pandas-dev/pandas) uses _pandas/pandas_
- [Requests](https://github.com/psf/requests) uses _requests/requests_
- The Python dependency management and packaging tool [Poetry](https://python-poetry.org/) supports either _appname_ or _src/appname_.

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
