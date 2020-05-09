"""
0021 Merge Two Sorted Lists
---------------------------

https://leetcode.com/problems/merge-two-sorted-lists/

Easy

Merge two sorted linked lists and return it as a new list. The new list should be made
by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Comments:
This problem doesn't seem relevant to modern programming languages. It's not necessary
to worry about creating linked lists in Python or JavaScript, they do it automatically.
The use of "ListNode" was also unclear. Using 1->2->4 as an input is not valid Python.
"""
from operator import attrgetter
from typing import List


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two lists
        ---
        solution = (
            "https://leetcode.com/problems/merge-two-sorted-lists/discuss/454114/"
            "Python3-(80100)-5-lines-recursive"
        )
        """
        if not (l1 and l2):
            return l1 or l2
        l1, l2 = sorted((l1, l2), key=attrgetter("val"))
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

    def easyMerge(self, l1, l2: List[int]) -> List[int]:
        """Merge two lists
        ---
        Merging lists in Python is simple! Just add them together.
        The `sorted()` function will sort the new list.
        """
        return sorted(l1 + l2)


if __name__ == "__main__":
    l1 = ListNode([1, 2, 4])
    l2 = ListNode([1, 3, 4])
    l1_easy = [1, 2, 4]
    l2_easy = [1, 3, 4]
    print(f"Merged list: {Solution().easyMerge(l1_easy, l2_easy)}")
    print(f"Merged list: {Solution().mergeTwoLists(l1, l2)}")
