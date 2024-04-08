import pytest
from lib.anagram_detection import anagram_detection

@pytest.mark.parametrize('string1, string2, expected_result', [
    ('foefet', 'toffee', True),
    ('foefer', 'toffee', False),
])
def test_anagram_detection_returns_True_if_strings_are_anagrams_of_each_other(string1, string2, expected_result):
    result = anagram_detection(string1, string2)
    assert result == expected_result