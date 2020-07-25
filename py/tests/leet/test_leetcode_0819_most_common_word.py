from typing import List

import pytest  # type: ignore

from algorythms.leet.leetcode_0819_most_common_word import Solution  # type: ignore


@pytest.mark.parametrize(
    "paragraph_string,banned_list,output_string",
    [
        ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
        ("a, a, a, a, b,b,b,c, c", ["a"], "b"),
        ("this this word word word this is is occurs twice.", ["this", "word"], "is"),
    ],
)
def test_mostCommonWord(
    paragraph_string: str, banned_list: List[str], output_string: str
) -> None:
    assert Solution.mostCommonWord(paragraph_string, banned_list) == output_string
