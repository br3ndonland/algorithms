"""
0020 Valid Parentheses
----------------------

https://leetcode.com/problems/valid-parentheses/

Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine
if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""
from typing import Dict


class Solution:
    def isValid(self, s: str) -> bool:
        """Check that open characters in a string are properly closed.
        ---
        Arguments:
        - s: str. A string of characters to check.
        Returns:
        - Boolean
        """
        matches = ["()", "[]", "{}"]
        while any(match in s for match in matches):
            for match in matches:
                s = s.replace(match, "")
        return not len(s)


if __name__ == "__main__":
    tests: Dict[str, bool] = {
        "()": True,
        "()[]{}": True,
        "(]": False,
        "([)]": False,
        "{[]}": True,
        "": True,
        "[": False,
        "[[": False,
        "([]": False,
        "()()()([])": True,
        "(([]){})": True,
    }
    for test in tests:
        print(
            f"Test: {test}\n",
            f"Expected: {tests[test]}\n",
            f"Result: {Solution().isValid(test)}\n",
        )
