import inspect

from modify import swap_all_cases

TEST_SUITE_NAME = "Modify Tests"


def body_of(func):
    """The function's source without its `def` line."""
    lines = inspect.getsource(func).splitlines()
    start = next(i for i, line in enumerate(lines) if line.rstrip().endswith(":"))
    return "\n".join(lines[start + 1:])


def test_swap_all_cases():
    """swap_all_cases - swaps every letter's case using a regex, upper and lower once each"""
    assert swap_all_cases("Hello") == "hELLO"
    assert swap_all_cases("hELLO") == "Hello"
    assert swap_all_cases("Now What?") == "nOW wHAT?"
    assert swap_all_cases("SpONGeBoB TeXT") == "sPongEbOb tExt"
    assert swap_all_cases("123") == "123"
    assert swap_all_cases("") == ""

    body = body_of(swap_all_cases)
    assert body.count(".upper()") == 1
    assert body.count(".lower()") == 1
    # Python has str.swapcase(), which would skip the exercise entirely.
    assert "swapcase" not in body
    assert "re.sub" in body
