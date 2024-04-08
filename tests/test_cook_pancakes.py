from lib.cook_pancakes import *
import pytest

@pytest.mark.parametrize('num_of_pancakes, num_of_concurrent_pancakes, expected_result', [
    (1, 2, 2),
    (2, 2, 2),
    (4, 2, 4),
    (7, 3, 5),
    (3, 2, 3),
    (4, 3, 3),
    (599, 45, 27),
])
def test_cook_pancakes_returns_time_needed_to_cook_n_pancakes(num_of_pancakes, num_of_concurrent_pancakes, expected_result):
    result = cook_pancakes(num_of_pancakes, num_of_concurrent_pancakes)
    assert result == expected_result