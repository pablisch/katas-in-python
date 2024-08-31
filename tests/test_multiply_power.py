import pytest
from lib.multiply_power import *

@pytest.mark.parametrize('n, expected_result', [
    (3, 15),
    (10, 250),
    (200, 25000),
    (-50, -1250),
    (-10, -250),
])
def test_multiply_power_returns_n_times_5_to_the_power_of_the_num_of_digits(n, expected_result):
    result = multiply_power(n)
    assert result == expected_result