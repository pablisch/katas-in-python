import pytest
from lib.some_stereometry import stereometry

@pytest.mark.parametrize('radius, distance_between_centres, expected_s_area, expected_c_area, expected_perimeter', [
    (2, 1, 50.265, 9.425, 10.883),
])
def test_stereometry_returns_a_tuple_containing_the_areas_of_sphere_and_circle_and_the_perimemter_of_the_circle(radius, distance_between_centres, expected_s_area, expected_c_area, expected_perimeter):
    result = stereometry(radius, distance_between_centres)
    assert result == (expected_s_area, expected_c_area, expected_perimeter)