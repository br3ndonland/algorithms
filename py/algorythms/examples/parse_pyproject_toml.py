from pathlib import Path
from typing import Any, Dict

import toml


def load_pyproject(pyproject_path: Path = Path("pyproject.toml")) -> Dict[str, Any]:
    """Load pyproject.toml into a dictionary, with a default dict as a fallback."""
    try:
        return dict(toml.load(pyproject_path))
    except Exception:
        return {
            "tool": {"poetry": {"name": "algorythms", "description": "", "version": ""}}
        }
