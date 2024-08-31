import pytest
from lib.is_cube import *

@pytest.mark.parametrize('volume, side, expected_result', [
    (-12, 2, False),
    (8, 3, False),
    (8, 2, True),
    (1, 1, True),
    (125, 5, True),
    (12, -1, False),
    (0, 0, False),
    (-8, -2, False),
])
def test_is_cube_returns_bool_of_cubeness(volume, side, expected_result):
    result = is_cube(volume, side)
    assert result == expected_result