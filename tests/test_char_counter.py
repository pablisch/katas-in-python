import pytest
from lib.char_counter import validate_word

@pytest.mark.parametrize('word, expected_result', [
    ('word', True),
    ('swords', False),
    ('Words', True),
])
def test_validate_word_returns_true_when_letter_count_is_same_for_all_chars_in_word(word, expected_result):
    result = validate_word(word)
    assert result == expected_result