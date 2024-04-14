import pytest
from lib.sum_of_multiples import sum_of_multiples

@pytest.mark.parametrize('n, m, expected_result', [
(2, 9, 20),
(4, 123, 1860),
(4, -7, "INVALID"),
])
def test__returns(n, m, expected_result):
    result = sum_of_multiples(n, m)
    assert result == expected_result