from lib.is_letter import is_letter
import pytest

@pytest.mark.parametrize('string, expected_result', [
    ('r', True),
    ('3', False),
])
def test_is_letter_returns_True_if_string_is_a_letter(string, expected_result):
    result = is_letter(string)
    assert result == expected_result