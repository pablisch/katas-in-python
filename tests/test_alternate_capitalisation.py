from lib.alternate_capitalisation import alternate_capitalisation
import pytest

@pytest.mark.parametrize('string, expected_result', [
    ("abcdef", ['AbCdEf', 'aBcDeF']),
    ("abcdefg", ['AbCdEfG', 'aBcDeFg']),
])
def test_alternate_capitalisation_returns_array_of_two_alternately_capitalised_versions(string, expected_result):
    result = alternate_capitalisation(string)
    assert result == expected_result