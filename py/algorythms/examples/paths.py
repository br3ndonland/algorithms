from importlib import import_module
from pathlib import Path
from typing import List


def get_modules(directory: Path = Path(__file__).parent) -> List[str]:
    """Get a list of Python modules in a directory, excluding `__init__.py`.
    ---
    https://docs.python.org/3/library/pathlib.html

    To recurse into subdirectories, try `directory.glob("**/*.py")`.
    """
    return [
        Path(file).stem
        for file in directory.iterdir()
        if Path(file).suffix == ".py" and Path(file).stem != "__init__"
    ]


def import_modules(modules: List[str]) -> List:
    """Import a list of Python modules.
    ---
    """
    try:
        return [import_module(module) for module in modules]
    except ImportError:
        raise


if __name__ == "__main__":
    modules = get_modules()
    print(f"{len(import_modules(modules))} modules imported")
    print(f"Total of {len(list(Path(__file__).parent.iterdir()))} in this directory.")
