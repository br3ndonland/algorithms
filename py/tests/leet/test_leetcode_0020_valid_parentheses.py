import pytest  # type: ignore

from algorythms.leet.leetcode_0020_valid_parentheses import Solution  # type: ignore


@pytest.mark.parametrize(
    "input_string,output_boolean",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("[", False),
        ("[[", False),
        ("([]", False),
        ("()()()([])", True),
        ("(([]){})", True),
    ],
)
def test_isValid(input_string: str, output_boolean: bool) -> None:
    assert Solution.isValid(input_string) == output_boolean
