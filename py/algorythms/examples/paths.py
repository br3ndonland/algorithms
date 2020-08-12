from pathlib import Path, PurePath
from typing import List


def get_modules(dirpath: Path = Path(PurePath(__file__).parent)) -> List[str]:
    """Get a list of Python modules in a directory and sub-directories,
    excluding __init__.py.
    ---
    https://docs.python.org/3/library/pathlib.html
    """
    return [file.name[:-3] for file in dirpath.glob("**/*[!__init__].py")]


if __name__ == "__main__":
    print(get_modules())
