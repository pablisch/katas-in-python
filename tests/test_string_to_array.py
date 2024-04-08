from lib.string_to_array import string_to_array
import pytest

@pytest.mark.parametrize('string, expected_result', [
    ("Robin Singh", ["Robin", "Singh"]),
    ("I love arrays they are my favorite", ["I", "love", "arrays", "they", "are", "my", "favorite"]),
])
def test_string_to_array_returns_an_array_of_words_from_input_string(string, expected_result):
    result = string_to_array(string)
    assert result == expected_result