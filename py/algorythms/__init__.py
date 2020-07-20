"""
algorythms
---
Miscellaneous curiosities from the world of computer programming
https://github.com/br3ndonland/algorithms
"""
from importlib.metadata import version


def package_version() -> str:
    """
    Calculate version number based on pyproject.toml.
    ---
    During `poetry install`, Poetry installs the project as if it were a package itself.
    You can then pull from the package metadata.

    See [poetry#1036](https://github.com/python-poetry/poetry/issues/1036) and
    [poetry#144](https://github.com/python-poetry/poetry/issues/144) for more info.
    """
    return version(__package__)


__version__ = package_version()
