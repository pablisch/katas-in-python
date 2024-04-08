from lib.coloured_hexes import coloured_hexes
import pytest

@pytest.mark.parametrize('hex_string, expected_result', [
    ('000 000 000', 'black'),
    ('021 021 021', 'white'),
    ('021 021 020', 'yellow'),
    ('000 147 000', 'green'),
    ('', 'black'),
])
def test_coloured_hexes_returns_a_string_indicating_the_dominant_colour(hex_string, expected_result):
    result = coloured_hexes(hex_string)
    assert result == expected_result