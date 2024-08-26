import pytest
from lib.vowel_code import *

@pytest.mark.parametrize('string, expected_result', [
    ("hello", "h2ll4"),
])
def test_encode_returns_encoded_string(string, expected_result):
    result = encode(string)
    assert result == expected_result

@pytest.mark.parametrize('string, expected_result', [
    ("h2ll4", "hello"),
])
def test_decode_returns_encoded_string(string, expected_result):
    result = decode(string)
    assert result == expected_result

@pytest.mark.parametrize('string, expected_result', [
    ("hello", "h2ll4"),
])
def test_encode_with_translate_returns_encoded_string(string, expected_result):
    result = encode_with_translate(string)
    assert result == expected_result

@pytest.mark.parametrize('string, expected_result', [
    ("h2ll4", "hello"),
])
def test_decode_with_translate_returns_encoded_string(string, expected_result):
    result = decode_with_translate(string)
    assert result == expected_result