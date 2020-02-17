from typing import List


def hello_lines(n: int) -> List[str]:
    """Hello lines
    ---
    This was a question in an online software engineering job assessment.
    - Accept an integer n <= 100 from user input.
    - Return "Hello" n times.
    """
    lines = []
    if n <= 100:
        for i in range(n):
            lines.append("Hello")
    else:
        print("Please enter an integer less than, or equal to, 100.")
    for line in lines:
        print(line)
    return lines


def user_input():
    try:
        n = input("Please enter an integer: ")
        hello_lines(int(n))
    except Exception as e:
        print(f"An exception occurred:\n{e}.\nPlease enter an integer.")


if __name__ == "__main__":
    user_input()
