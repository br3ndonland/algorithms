"""
Using filter expressions in list comprehensions
-----------------------------------------------

https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/46
"""

from typing import Any, Dict, Iterator, List, Union

sample_dict: Dict[str, List[Union[str, List[str]]]] = {
    "Processes": [
        ["29173", "root", "0:00", "gunicorn -c /gunicorn_conf.py main:app"],
        ["29207", "root", "0:00", "gunicorn -c /gunicorn_conf.py main:app"],
        ["29208", "root", "0:00", "gunicorn -c /gunicorn_conf.py main:app"],
    ],
    "Titles": ["PID", "USER", "TIME", "COMMAND"],
}


def filter_comprehension(
    sample_dict: Dict[str, List[Union[str, List[str]]]],
    list_in_dict: str = "Processes",
    filter_string: str = "gunicorn",
) -> List[Iterator[Any]]:
    return [filter(lambda i: filter_string in i, j) for j in sample_dict[list_in_dict]]


def get_gunicorn_conf_path(path: str) -> str:
    first_part, partition, last_part = path.partition("-c")
    return last_part.strip().split()[0]


if __name__ == "__main__":
    path = list(filter_comprehension(sample_dict, list_in_dict="Processes")[0])[0]
    print(f"Gunicorn config file path: {get_gunicorn_conf_path(path)}")
