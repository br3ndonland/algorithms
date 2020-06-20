"""This was a question in an online software engineering job assessment."""
from typing import List


def user_input() -> int:
    """Accept an integer n <= 100 from user input."""
    n = int(input("Please enter an integer: "))
    if n <= 100:
        hello_lines(n)
    else:
        print("Please enter an integer less than, or equal to, 100.")
    return n


def hello_lines(n: int) -> List[str]:
    """Hello lines
    ---
    This was a question in an online software engineering job assessment.
    - Accept an integer n <= 100 from user input.
    - Return "Hello" n times.
    """
    return ["Hello" for i in range(n) if n <= 100]


if __name__ == "__main__":
    user_input()
