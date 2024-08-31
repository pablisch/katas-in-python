import pytest
from lib.calculator import *

@pytest.mark.parametrize('num1, num2, op, expected_result', [
    (6, 2, "+", 8),
    (6, 2, 5, "unknown value"),
    (6, 2, "&", "unknown value"),
    (5, 0, "/", "undefined"),
])
def test_calculator_returns_the_correct_value(num1, num2, op, expected_result):
    result = calculator(num1, num2, op)
    assert result == expected_result

@pytest.mark.parametrize('num1, num2, op, expected_result', [
    (6, 2, "+", 8),
    (6, 2, 5, "unknown value"),
    (6, 2, "&", "unknown value"),
    # (5, 0, "/", "undefined"),
])
def test_calculator_cw_returns_the_correct_value(num1, num2, op, expected_result):
    result = calculator_cw(num1, num2, op)
    assert result == expected_result