import pytest
from lib.bartender import *

@pytest.mark.parametrize('input, expected_result', [
    ("jabroni", "Patron Tequila"),
    ("School Counselor", "Anything with Alcohol"),
    ("School CounSelor", "Anything with Alcohol"),
])
def test_bartender_returns_correct_drinks_order(input, expected_result):
    result = bartender(input)
    assert result == expected_result