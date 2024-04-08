from lib.largest_sum_pair import largest_sum_pair
import pytest

@pytest.mark.parametrize('input_list, expected_result', [
    ([10, 14, 2, 23, 19],  42),
    ([99, 2, 2, 23, 19], 122),
])
def test_largest_sum_pair_returns_the_sum_of_the_two_largest_nums_in_a_list(input_list, expected_result):
    result = largest_sum_pair(input_list)
    assert result == expected_result