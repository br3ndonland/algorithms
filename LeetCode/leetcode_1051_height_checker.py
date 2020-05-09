"""
1051. Height Checker
--------------------

https://leetcode.com/problems/height-checker/
Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students not standing in the right positions.
(This is the number of students that must move in order for all students to be standing
in non-decreasing order of height.)

Example 1:
Input: [1,1,4,2,1,3]
Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right
positions.

Note:
1 <= heights.length <= 100
1 <= heights[i] <= 100

- [Typing](https://docs.python.org/3/library/typing.html?highlight=typing#module-typing)
- [`zip()`](https://docs.python.org/3/library/functions.html#zip)
- LeetCode requires the same camelCase class and function titles to pass
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """Height checker
        -----------------
        - type heights: List[int]
        - rtype: int
        """
        out = 0
        for i, j in zip(heights, sorted(heights)):
            if i != j:
                out += 1
        return out


if __name__ == "__main__":
    heights = [1, 1, 4, 2, 1, 3, 40, 10]
    print(f"Number of students out of order: {Solution().heightChecker(heights)}")
