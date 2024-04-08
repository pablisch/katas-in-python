import pytest
from lib.array_element_parity import *

@pytest.mark.parametrize('data, expected_result', [
    ([1, -1, 2, -2, 3], 3),
    ([-3, 1, 2, 3, -1, -4, -2], -4),
    ([-110, 110, -38, -38, -62, 62, -38, -38, -38],  -38),
    ([1, -1, 2, -2, 3, 3], 3),
    ([-9, -105, -9, -9, -9, -9, 105],  -9),
])
def test_find_unique_value(data, expected_result):
    result = solve(data)
    assert result == expected_result