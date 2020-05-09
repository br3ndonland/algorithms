/**
 * ### 0819 Most Common Word
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 * @description
 * [Problem](https://leetcode.com/problems/most-common-word/)
 */
const mostCommonWord = (paragraph, banned) => {
  // Split paragraph into list on spaces or punctuation, make lowercase
  const words = paragraph.toLowerCase().split(/[!?',;.\s]+/)
  // Remove banned words
  const wordsNotBanned = words.filter(
    (word) => !banned.includes(word) && word.length > 0
  )
  // Create a map with each unique word and the number of occurrences
  const wordsMap = new Map(
    wordsNotBanned.map((word) => [
      word,
      wordsNotBanned.filter((words) => words === word).length,
    ])
  )
  // Identify the most common non-banned word
  // Spreading and reducing can identify the highest value, but can't return the key
  // const topValue = [...wordsMap].reduce((max, i) => (i[1] > max ? i[1] : max), ``)
  top = ["word", 0]
  for (const [key, value] of wordsMap) {
    value > top[1] ? (top = [key, value]) : top
  }
  return top[0]
}

const paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
const banned = ["hit"]
const test1 = "a, a, a, a, b,b,b,c, c"
const test1_banned = ["a"]
console.log(`Most common word: ${mostCommonWord(test1, test1_banned)}`)
