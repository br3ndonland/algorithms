import pytest

from algorythms.examples import case


@pytest.mark.parametrize(
    "input_str,output_str",
    [
        ("hello world", "HelloWorld"),
        ("Hello, World!", "HelloWorld"),
        ("snake_case", "SnakeCase"),
    ],
)
def test_pascal(input_str: str, output_str: str) -> None:
    """Assert that strings are successfully converted to PascalCase."""
    assert case.pascal(input_str) == output_str


@pytest.mark.parametrize(
    "input_str,output_str",
    [
        ("AlreadyPascalCase", "AlreadyPascalCase"),
        ("HelloPascal", "HelloPascal"),
        ("PasCalCase", "PascalCase"),
    ],
)
@pytest.mark.xfail(reason="String is already PascalCase")
def test_pascal_already_pascal(input_str: str, output_str: str) -> None:
    """Fail when string is already PascalCase.
    The algorithm doesn't have an easy way of determining whether or not
    a string is correctly PascalCase. For example, the input string could
    be `PasCalCase`.
    """
    assert case.pascal(input_str) == output_str


@pytest.mark.parametrize(
    "input_str,output_str",
    [
        ("already_snake_case", "already_snake_case"),
        ("camelCase", "camel_case"),
        ("pascalCase", "pascal_case"),
        ("Foo Bar", "foo_bar"),
        ("A man, A Plan, A Canal, Panama", "a_man_a_plan_a_canal_panama"),
    ],
)
def test_snake(input_str: str, output_str: str) -> None:
    """Assert that strings are successfully converted to snake_case."""
    assert case.snake(input_str) == output_str


@pytest.mark.parametrize(
    "input_str,output_str",
    [
        ("already_snake_case", "already_snake_case"),
        ("AlreadyPascalCase", "already_pascal_case"),
        ("HelloPascal", "hello_pascal"),
        ("InCorrectPasCalCase", "in_correct_pas_cal_case"),
    ],
)
def test_pascal_to_snake(input_str: str, output_str: str) -> None:
    """Assert that strings are successfully converted from PascalCase to snake_case."""
    assert case.pascal_to_snake(input_str) == output_str
