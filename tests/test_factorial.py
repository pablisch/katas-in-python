import pytest
from lib.factorial import *

@pytest.mark.parametrize('number, expected_result', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
])
def test_factorial_function_returns_correct_factorial(number, expected_result):
    result = factorial(number)
    assert result == expected_result

@pytest.mark.parametrize('number, expected_result', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
])
def test_factorial_function_returns_correct_factorial_using_reduce(number, expected_result):
    result = factorial_with_reduce(number)
    assert result == expected_result