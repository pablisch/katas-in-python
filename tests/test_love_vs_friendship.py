import pytest
from lib.love_vs_friendship import get_word_value

@pytest.mark.parametrize('word, expected_result', [
    ('love', 54),
    ('friendship', 108),
])
def test_get_word_value_returns_the_word_value_based_on_letter_alphabet_positions(word, expected_result):
    result = get_word_value(word)
    assert result == expected_result