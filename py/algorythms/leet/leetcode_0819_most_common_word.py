"""
0819. Most Common Word
----------------------

https://leetcode.com/problems/most-common-word/

Easy

Given a paragraph and a list of banned words, return the most frequent word that is not
in the list of banned words. It is guaranteed there is at least one word that isn't
banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive. The answer is in lowercase.

Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word
in the paragraph. Note that words in the paragraph are not case sensitive, that
punctuation is ignored (even if adjacent to words, such as "ball,"), and that "hit"
isn't the answer even though it occurs more because it is banned.

Note:
- 1 <= paragraph.length <= 1000.
- 0 <= banned.length <= 100.
- 1 <= banned[i].length <= 10.
- The answer is unique, and written in lowercase (even if its occurrences in paragraph
  may have uppercase symbols, and even if it is a proper noun.)
- paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
- There are no hyphens or hyphenated words.
- Words only consist of letters, never apostrophes or other punctuation symbols.
"""
import re
from collections import Counter
from typing import Dict, List


class Solution:
    @staticmethod
    def mostCommonWord(paragraph: str, banned: List[str]) -> str:
        """Most common word
        -------------------
        Given a paragraph and a list of banned words, return the most frequent word
        that is not in the list of banned words.
        """
        # Split paragraph into list on spaces or punctuation and transform to lowercase
        # Remove banned words: either lambda or list comprehension will work
        words: List[str] = list(
            filter(
                lambda word: word not in banned and len(word) > 0,
                re.split(r"[!?',;.\s]+", paragraph.lower()),
            )
        )
        # Use dict comprehension to create dict and count occurrences of each word
        # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        freq: Dict[str, int] = {word: words.count(word) for word in words}
        # Identify the most frequent non-banned word
        top = Counter(freq).most_common(1)
        return [i[0] for i in top][0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    test1 = "a, a, a, a, b,b,b,c, c"
    test1_banned = ["a"]
    print(f"Most common word: {Solution.mostCommonWord(paragraph, banned)}")
