"""
algorythms
---
Miscellaneous curiosities from the world of computer programming
https://github.com/br3ndonland/algorithms
"""
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseSettings

from algorythms.examples.parse_pyproject_toml import load_pyproject


class Settings(BaseSettings):
    """Instantiate a Pydantic Settings model."""

    pyproject: Dict[str, Any] = load_pyproject(pyproject_path=Path("pyproject.toml"))
    title: str = str(pyproject["tool"]["poetry"]["name"])
    description: str = str(pyproject["tool"]["poetry"]["description"])
    version: str = str(pyproject["tool"]["poetry"]["version"])


settings = Settings()
