import pytest
from lib.trilingual_democracy import trilingual_democracy

@pytest.mark.parametrize('group, expected_result', [
    ("FFF", "F"),
    ("IIK", "K"),
    ("DFK", "I"),
])
def test_trilingual_democracy_returns_char_denoting_language_spoken(group, expected_result):
    result = trilingual_democracy(group)
    assert result == expected_result