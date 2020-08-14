from importlib import import_module
from pathlib import Path, PurePath
from typing import List


def get_modules(dirpath: Path = Path(PurePath(__file__).parent)) -> List[str]:
    """Get a list of Python modules in a directory and sub-directories,
    excluding __init__.py.
    ---
    https://docs.python.org/3/library/pathlib.html
    """
    return [PurePath(file).stem for file in dirpath.glob("**/*[!__init__].py")]


def import_modules(modules: List[str]) -> List:
    """Import Python modules in a directory and sub-directories, excluding __init__.py.
    ---
    """
    try:
        return [import_module(module) for module in modules]
    except ImportError:
        raise


if __name__ == "__main__":
    modules = get_modules()
    print(modules)
    import_modules(modules)
