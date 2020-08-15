from importlib import import_module
from pathlib import Path
from typing import List


def get_modules(directory: Path = Path(__file__).parent) -> List[str]:
    """Get a recursive list of Python modules in a directory, excluding `__init__.py`.
    ---
    https://docs.python.org/3/library/pathlib.html

    TODO: glob is not matching all the modules in this directory
    """
    return [Path(file).stem for file in directory.glob("**/*[!__init__].py")]


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
    print(sorted(modules))
    print(f"{len(import_modules(modules))} modules imported")
