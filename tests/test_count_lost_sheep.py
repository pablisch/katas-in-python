import pytest
from lib.count_lost_sheep import lost_sheep

@pytest.mark.parametrize('friday, saturday, total, expected_result', [
    ([1,2],[3,4],15,5),
    ([3,1,2],[4,5],21,6),
    ([5,1,4],[5,4],29,10),
])
def test_lost_sheep_returns_num_of_lost_sheep(friday, saturday, total, expected_result):
    result = lost_sheep(friday, saturday, total)
    assert result == expected_result