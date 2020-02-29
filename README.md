# Algorithms

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![pre-commit](https://github.com/br3ndonland/algorithms/workflows/pre-commit/badge.svg)

Brendon Smith ([br3ndonland](https://github.com/br3ndonland/))

## Description

This repository was generated from my [GitHub template repository](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/) and contains solutions to common computer science algorithm problems in Python and JavaScript.

## Repository contents

- [.github/](.github): configuration files for [GitHub](https://github.com/).
  - [ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE)
    - [bug_report.md](.github/ISSUE_TEMPLATE/bug_report.md): template for filing a bug report issue on GitHub.
    - [feature_request.md](.github/ISSUE_TEMPLATE/feature_request.md): template for filing a feature request issue on GitHub.
  - [workflows/](.github/workflows)
    - [pre-commit.yml](.github/workflows/pre-commit.yml): [GitHub Actions](https://github.com/features/actions) workflow that runs pre-commit with each pull request or push to the master branch.
  - [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md): guidelines for behavior when contributing to open-source projects.
  - [CONTRIBUTING.md](.github/CONTRIBUTING.md): detailed instructions for using this repository.
- [examples/](examples): code samples that can be used to try out the Python tooling in this repo.
- [LeetCode/](LeetCode): solutions to algorithm problems on [LeetCode](https://leetcode.com/).
- [tutorials/](tutorials): notes and examples from tutorials.
- [.pre-commit-config.yaml](.pre-commit-config.yaml): configuration file for [pre-commit](https://pre-commit.com/) specifying [Git pre-commit hooks](https://www.git-scm.com/docs/githooks).
- [.prettierrc](.prettierrc): configuration file for [Prettier](https://prettier.io/docs/en/configuration.html).
- [LICENSE](LICENSE): [license](https://choosealicense.com/) file describing how the repository may be legally used.
- [Pipfile](Pipfile): [Pipenv](https://pipenv.readthedocs.io/) package list
- [README.md](README.md): this file, a concise description of the repository
- [setup.py](setup.py): this file helps Python understand your project structure and locate files, even if you're not going to publish your project as a Python package on [PyPI](https://pypi.org/). For example, if your tests are in a sub-directory like _test/_, adding _setup.py_ helps pytest locate Python modules to load when running tests. To tell Python to read your _setup.py_ file, simply run `pip install -e .` as described in [quickstart](#quickstart). For more info, see the [`pip install -e` docs](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) and the [pytest docs on good integration practices](https://docs.pytest.org/en/latest/goodpractices.html).

## Quickstart

```sh
❯ cd path/to/repo
❯ pipenv install --dev
❯ pipenv shell
template-python-hash ❯ pre-commit install
```

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
