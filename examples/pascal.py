#!/usr/bin/env python3
from re import sub


def pascal(s: str) -> str:
    """Convert a string to PascalCase."""
    return sub(r"(_|-)+", " ", s).title().replace(" ", "")
