import pytest
from lib.find_odd_int import *

@pytest.mark.parametrize('lst, expected_result', [
    ([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5], 5),
    ([1,1,2,-2,5,2,4,4,-1,-2,5], -1),
])
def test_find_odd_int_returns_odd_int(lst, expected_result):
    result = find_odd_int(lst)
    assert result == expected_result

@pytest.mark.parametrize('lst, expected_result', [
    ([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5], 5),
    ([1,1,2,-2,5,2,4,4,-1,-2,5], -1),
])
def test_find_odd_int_counter_returns_odd_int(lst, expected_result):
    result = find_odd_int_counter(lst)
    assert result == expected_result

@pytest.mark.parametrize('lst, expected_result', [
    ([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5], 5),
    ([1,1,2,-2,5,2,4,4,-1,-2,5], -1),
])
def test_find_odd_int_iter_count_returns_odd_int(lst, expected_result):
    result = find_odd_int_iter_count(lst)
    assert result == expected_result