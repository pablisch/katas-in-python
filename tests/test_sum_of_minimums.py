import pytest
from lib.sum_of_minimums import *

@pytest.mark.parametrize('lst, expected_result', [
    ([], 0),
])
def test_sum_of_minimums_returns_the_sum_of_minimum_values(lst, expected_result):
    result = sum_of_minimums(lst)
    assert result == expected_result