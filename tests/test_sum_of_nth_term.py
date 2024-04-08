import pytest
from lib.sum_of_nth_term import *

@pytest.mark.parametrize('n, expected_result', [
    (1, '1.00'),
    (2, '1.25'),
    (5, '1.57'),
])
def test_sum_of_nth_term_returns_the_sum_of_nth_term_given(n, expected_result):
    result = sum_of_nth_term(n)
    assert result == expected_result

@pytest.mark.parametrize('n, expected_result', [
    (1, '1.00'),
    (2, '1.25'),
    (5, '1.57'),
])
def test_series_sum_returns_the_sum_of_nth_term_given(n, expected_result):
    result = series_sum(n)
    assert result == expected_result