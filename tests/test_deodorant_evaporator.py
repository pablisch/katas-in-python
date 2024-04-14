import pytest
from lib.deodorant_evaporator import deodorant_evaporation_threshold

@pytest.mark.parametrize('content, loss_rate, threshold, expected_result', [
(10, 10, 5, 29),
])
def test_deodorant_evaporation_threshold_returns_day_that_deodorant_stops_working(content, loss_rate, threshold, expected_result):
    result = deodorant_evaporation_threshold(content, loss_rate, threshold)
    assert result == expected_result