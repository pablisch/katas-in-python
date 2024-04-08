from lib.what_floor import what_floor
import pytest

@pytest.mark.parametrize('floor, expected_result', [
    (1, 0),
    (0, 0),
    (5, 4),
    (15, 13),
    (-3, -3),
    (17, 15),
    (13, 11),
    (12, 11),
])
def test_what_floor_returns_the_floor_number_given_a_logical_floor_number(floor, expected_result):
  result = what_floor(floor)
  assert result == expected_result