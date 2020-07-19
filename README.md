# Algorithms

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![pre-commit](https://github.com/br3ndonland/algorithms/workflows/pre-commit/badge.svg)

Brendon Smith ([br3ndonland](https://github.com/br3ndonland/))

## Description

This repository contains solutions to common computer science algorithm problems in Python and JavaScript. It's also a useful source of default tooling for my projects.

## Directory structure

You'll notice that there's a subdirectory named _src_. The convention in the Python community is to put application code either in _repo/appname_, or in _repo/src/appname_. Typically the _repo/appname_ directory contains the source code used to build the Python package _appname_. Some examples:

- [FastAPI](https://github.com/tiangolo/fastapi) uses _fastapi/fastapi_
- [Flask](https://github.com/pallets/flask) uses _flask/src/flask_
- [Pandas](https://github.com/pandas-dev/pandas) uses _pandas/pandas_
- [Requests](https://github.com/psf/requests) uses _requests/requests_
- The Python dependency management and packaging tool [Poetry](https://python-poetry.org/) offers either _repo/appname_ or _repo/src/appname_.

JavaScript typically uses _repo/src_.

This project contains both Python and JavaScript code, so _algorithms/src_ is used as a directory for both. The _algorithms/src/algorythms_ directory contains Python code, and the _algorithms/src/ecmarithms_ directory contains JavaScript. Tests for both languages are in the corresponding directories in _algorithms/tests_.

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
