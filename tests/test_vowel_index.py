import pytest
from lib.vowel_index import *

@pytest.mark.parametrize('word, expected_result', [
    ('Mmmm', []),
    ('Super', [2, 4]),
])
def test_vowel_indices_returns_a_list_of_vowel_positions(word, expected_result):
    result = vowel_indices(word)
    assert result == expected_result

@pytest.mark.parametrize('word, expected_result', [
    ('Mmmm', []),
    ('Super', [2, 4]),
])
def test_vowel_positions_returns_a_list_of_vowel_positions(word, expected_result):
    result = vowel_positions(word)
    assert result == expected_result