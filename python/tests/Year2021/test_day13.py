import pytest
from ..common import validate_problem_test


@pytest.mark.parametrize("part", ["a"])  # b has no return value
@pytest.mark.parametrize("test", [1])
def test_day13(part, test):
    result, expected = validate_problem_test("2021", "13", part, str(test))
    assert result == expected
