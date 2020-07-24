from algorythms.examples import hello_lines  # type: ignore


def test_hello_lines() -> None:
    assert len(hello_lines.hello_lines(42)) == 42


def test_hello_lines_incorrect_range() -> None:
    assert len(hello_lines.hello_lines(101)) == 0
