#!/usr/bin/env python3
import functools
import re


def pascal(s: str) -> str:
    """Convert a string to PascalCase."""
    return (
        re.sub(pattern=r"(_|-)+", repl=" ", string=re.sub(r"[!?',;.]+", "", s))
        .title()
        .replace(" ", "")
    )


def snake(s: str) -> str:
    """Convert a string to snake_case."""
    return "_".join(
        re.sub(
            pattern=r"([A-Z][a-z]+)",
            repl=r" \1",
            string=re.sub(
                r"([A-Z]+)", r" \1", re.sub(r"[!?',;.]+", "", s.replace("-", " "))
            ),
        ).split()
    ).lower()


def pascal_to_snake(s: str) -> str:
    """Convert a string from PascalCase to snake_case."""
    return functools.reduce(
        lambda x, y: x + ("_" if y.isupper() and not x.isupper() else "") + y, s
    ).lower()
