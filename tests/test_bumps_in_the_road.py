import pytest
from lib.bumps_in_the_road import journey

@pytest.mark.parametrize('road, expected_result', [
    ("n", "Woohoo!"),
    ("_nnnnnnn_n__n______nn__nn_nnn", "Car Dead"),
])
def test_journey_returns_the_appropriate_result(road, expected_result):
    result = journey(road)
    assert result == expected_result