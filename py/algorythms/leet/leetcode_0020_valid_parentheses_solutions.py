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
from typing import Dict, Generator, List


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


class GeneratorSolution:
    def isValid(self, s: str) -> bool:
        """Check that open characters in a string are properly closed.
        ---
        Arguments:
        - s: str. A string of characters to check.
        Returns:
        - Boolean
        """
        if len(s) == 1:
            return False
        matches = ["()", "[]", "{}"]
        misses = []
        remover = self.removeMatches(s, matches)
        for i in remover:
            misses.append(i)
        return not len(misses) or ("", "") in misses

    def removeMatches(self, s: str, matches: List[str]) -> Generator:
        """Remove matching characters from a string.
        ---
        Arguments:
        - s: str. A string of characters to check for matches.
        - matches: List[str]. A list of strings to match against s.
        Returns:
        - Generator with replaced string and characters that don't match.
        See also:
        [Python 3 docs](https://docs.python.org/3/reference/expressions.html),
        [Real Python](https://realpython.com/introduction-to-python-generators/)
        """
        miss = ""
        while any(match in s for match in matches):
            for match in matches:
                s = s.replace(match, "")
        if len(s):
            miss += s
        yield s, miss


class MyFriendsSolution:
    def isValid(self, s: str) -> bool:
        """Check that open characters in a string are properly closed.
        ---
        Arguments:
        - s: str. A string of characters to check.
        Returns:
        - Boolean
        """
        return self.removeMatching(s)

    def removeMatching(self, s: str) -> bool:
        if s.find("()") != -1 or s.find("{}") != -1 or s.find("[]") != -1:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
            if len(s) == 0:
                return True
            else:
                return self.removeMatching(s)
        return s == ""


class LeetCodeSolution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        [Source](https://leetcode.com/articles/valid-parentheses/)
        """
        # The stack to keep track of opening brackets.
        stack: List[str] = []
        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}
        # For every bracket in the expression.
        for char in s:
            # If the character is an closing bracket
            if char in mapping:
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else "#"
                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)
        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


class CommSolution1:
    def isValid(self, s: str) -> bool:
        """Check that open characters in a string are properly closed.
        ---
        Arguments:
        - s: str. A string of characters to check.
        Returns:
        - Boolean
        CommSolution1 = (
            "https://leetcode.com/problems/valid-parentheses/discuss/9588/"
            "Python-concise-solution-using-stack./10529"
        )
        """
        if not s:
            return True
        for i in ["()", "[]", "{}"]:
            idx = s.find(i)
            if idx > -1:
                return self.isValid(s[:idx] + s[idx + 2 :])  # noqa: E203
        return False


class CommSolution2:
    def isValid(self, s: str) -> bool:
        """Check that open characters in a string are properly closed.
        ---
        Arguments:
        - s: str. A string of characters to check.
        Returns:
        - Boolean
        CommSolution2 = (
            "https://leetcode.com/problems/valid-parentheses/discuss/9203/"
            "Simple-Python-solution-with-stack"
        )
        The author's only comment outside the code block: "It's quite obvious."
        """
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict:
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


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
