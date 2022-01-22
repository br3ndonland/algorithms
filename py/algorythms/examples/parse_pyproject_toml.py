from pathlib import Path
from typing import Any, Dict

import tomli


def load_pyproject(pyproject_path: Path = Path("pyproject.toml")) -> Dict[str, Any]:
    """Load pyproject.toml into a dictionary, with a default dict as a fallback."""
    try:
        with open(pyproject_path, "rb") as pyproject_bytes:
            return dict(tomli.load(pyproject_bytes))
    except Exception:
        return {
            "tool": {"poetry": {"name": "algorythms", "description": "", "version": ""}}
        }
