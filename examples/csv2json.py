# /usr/bin/env python3
import csv
import json
import os


def input_path() -> str:
    """Read CSV input file and ensure path is valid."""
    path = input("Please input the path to a CSV file: ")
    if not os.path.isfile(path):
        return f"Not a valid file path: {path}"
    else:
        print(f"Valid file path: {path}")
        return path


def output_json(path: str) -> str:
    """Convert CSV to JSON."""
    with open(path) as csvfile:
        out: str = json.dumps([row for row in csv.DictReader(csvfile)])
        with open(f"{path}.json", "x") as jsonfile:
            jsonfile.write(out)
    print(f"CSV {path} converted to JSON.")
    return out


if __name__ == "__main__":
    path = input_path()
    output_json(path)
