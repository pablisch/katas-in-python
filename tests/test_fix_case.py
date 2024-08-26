import pytest
from lib.fix_case import *

@pytest.mark.parametrize('str_, expected_result', [
    ("coDe", "code"),
    ("cODe", "code"),
])
def test_solve_function_returns_single_case_string(str_, expected_result):
    result = solve(str_)
    assert result == expected_result