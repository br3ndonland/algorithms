from pathlib import Path

from algorythms.examples import paths


def test_get_modules(test_dir: Path = Path(__file__).parent) -> None:
    """Verify that `get_modules()` imports all the Python modules in a directory."""
    test_dir_list = list(test_dir.iterdir())
    get_modules_list = paths.get_modules(test_dir)
    assert len(get_modules_list) == len(test_dir_list) - 1
    assert len(paths.import_modules(get_modules_list)) == len(test_dir_list) - 1
