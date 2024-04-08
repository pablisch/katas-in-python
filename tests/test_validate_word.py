from lib.validate_word import validate_word
import pytest

@pytest.mark.parametrize('word, expected_result', [
    ("abcabc", True),
    ("Abcabc", True),
    ("AbcabcC", False),
    ("AbcCBa", True),
    ("?!?!?!", True),
    ("abc:abc", False),
])
def test_validate_word_returns_True_if_each_char_has_same_num_of_occurences(word, expected_result):
    result = validate_word(word)
    assert result == expected_result
