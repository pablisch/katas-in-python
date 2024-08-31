import pytest
from lib.most_digits import *

@pytest.mark.parametrize('lst, expected_result', [
    ([1, 10, 100], 100),
    ([9000, 8, 800], 9000),
    ([1, 200, 100000], 100000),
    ([1, 200, -300], 200),
])
def test_most_digits_returns_num_with_most_digits(lst, expected_result):
    result = most_digits(lst)
    assert result == expected_result

@pytest.mark.parametrize('lst, expected_result', [
    ([1, 10, 100], 100),
    ([9000, 8, 800], 9000),
    ([1, 200, 100000], 100000),
    ([1, 200, -300], 200),
])
def test_most_digits_cw_returns_num_with_most_digits(lst, expected_result):
    result = most_digits_cw(lst)
    assert result == expected_result