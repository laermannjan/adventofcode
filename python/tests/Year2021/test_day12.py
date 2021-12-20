import pytest
from ..common import validate_problem_test


@pytest.mark.skip
@pytest.mark.parametrize("part", ["a", "b"])
@pytest.mark.parametrize("test", [1, 2, 3])
def test_day12(part, test):
    assert validate_problem_test("2021", "12", part, str(test))
