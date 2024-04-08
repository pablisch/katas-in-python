import pytest
from lib.circle_area_inside_square import circle_area_inside_square

@pytest.mark.parametrize('area_of_square, expected_result', [
    (9, 7.06858347),
    (20, 15.70796327),
])
def test_circle_area_inside_square_returns_area_of_circle(area_of_square, expected_result):
    result = circle_area_inside_square(area_of_square)
    assert result == expected_result