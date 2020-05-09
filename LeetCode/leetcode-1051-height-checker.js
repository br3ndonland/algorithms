/*
1051 Height Checker: https://leetcode.com/problems/height-checker/
Students are asked to stand in non-decreasing order of heights for an annual
photo. Return the minimum number of students not standing in the right
positions. (This is the number of students that must move in order for all
students to be standing in non-decreasing order of height.)
Example 1:
  Input: [1,1,4,2,1,3]
  Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right
positions.
Note:
1 <= heights.length <= 100
1 <= heights[i] <= 100
*/

/**
 * ### 1051 Height Checker
 * @param {number[]} heights
 * @return {number}
 * @description
 * - [Problem](https://leetcode.com/problems/height-checker/)
 * - [Solution](https://leetcode.com/problems/height-checker/discuss/299723/Javascript-1-liner)
 * - [MDN - `sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
 * - [MDN - `reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
 * - [Rest](https://github.com/br3ndonland/udacity-google/blob/master/es6/es6-1-syntax.md): must use rest for array, otherwise will be sorted.
 */
const heightChecker = (heights) =>
  [...heights]
    .sort((a, b) => a - b)
    .reduce((out, i, j) => (i !== heights[j] ? out + 1 : out), 0)

const heightCheckerFail = (heights) => {
  out = 0
  for (const i of [...heights]) {
    if (i !== heights.sort()[i]) {
      out += 1
    }
  }
  return out
}

const example1 = [1, 1, 4, 2, 1, 3]
const example2 = [2, 1, 2, 1, 1, 2, 2, 1]
const example3 = [1, 2, 1, 2, 1, 1, 1, 2, 1]

console.log(heightChecker(example3))
console.log(heightCheckerFail(example3))
