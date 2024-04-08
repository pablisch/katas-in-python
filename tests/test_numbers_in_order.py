from lib.numbers_in_order import numbers_in_order
import pytest

@pytest.mark.parametrize('array, expected_result', [
    ([1, 4, 13, 97, 508, 1047, 20058], True),
    ([1, 2], True),
    ([1, 2, 3], True),
    ([2, 1], False),
    ([56, 98, 123, 67, 742, 1024, 32, 90969], False),
])
def test_numbers_in_order_return_True_if_nums_in_ascending_order(array, expected_result):
    result = numbers_in_order(array)
    assert result == expected_result