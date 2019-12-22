/**
 * ### 0021 Merge two sorted lists
 * [Problem](https://leetcode.com/problems/merge-two-sorted-lists/)
 * @summary
 * This problem was dumb. It seems more oriented towards Java or something.
 * I don't need to worry about creating linked lists in Python or JavaScript.
 * The languages do it for me.
 * Supposedly [this solution](https://leetcode.com/problems/merge-two-sorted-lists/discuss/454584/JavaScript.-Awesome-Swapping-in-Place-Trick.) works, but I don't understand why.
 *
 * @description
 * Merge two sorted linked lists and return it as a new list. The new list
 * should be made by splicing together the nodes of the first two lists.
 * Example:
 * Input: 1->2->4, 1->3->4
 * Output: 1->1->2->3->4->4
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {[]} l1
 * @param {[]} l2
 * @returns {[]}
 */
const easyMerge = (l1, l2) => {
  return [...l1, ...l2].sort()
}

const l1_easy = [1, 2, 4]
const l2_easy = [1, 3, 4]
console.log(`Merged list: ${easyMerge(l1_easy, l2_easy)}`)
