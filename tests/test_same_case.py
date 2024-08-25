import pytest
from lib.same_case import *

@pytest.mark.parametrize('char1, char2, expected_result', [
    ('a', 'g', 1),
    ('a', 'S', 0),
    ('a', '!', -1),
])
def test_same_case_returns_correct_indicator_number(char1, char2, expected_result):
    result = same_case(char1, char2)
    assert result == expected_result

@pytest.mark.parametrize('char1, char2, expected_result', [
    ('a', 'g', 1),
    ('a', 'S', 0),
    ('a', '!', -1),
])
def test_same_case_concise_returns_correct_indicator_number(char1, char2, expected_result):
    result = same_case_concise(char1, char2)
    assert result == expected_result