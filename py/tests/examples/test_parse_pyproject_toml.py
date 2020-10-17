from pathlib import Path

from algorythms import settings
from algorythms.examples.parse_pyproject_toml import load_pyproject


def test_load_pyproject() -> None:
    """Assert that pyproject.toml is successfully loaded and parsed."""
    pyproject = load_pyproject(pyproject_path=Path("pyproject.toml"))
    assert pyproject == settings.pyproject
    assert str(pyproject["tool"]["poetry"]["name"]) == settings.title
    assert str(pyproject["tool"]["poetry"]["description"]) == settings.description
    assert str(pyproject["tool"]["poetry"]["version"]) == settings.version


def test_load_pyproject_error() -> None:
    """Assert that default dict is loaded when pyproject.toml is not found."""
    pyproject = load_pyproject(pyproject_path=Path("pyproject.toml"))
    pyproject_default = load_pyproject(pyproject_path=Path("error"))
    assert pyproject != pyproject_default
    assert pyproject_default == {
        "tool": {"poetry": {"name": "algorythms", "description": "", "version": ""}}
    }
