import pytest
from lib.even_numbers import get_last_n_even_numbers

@pytest.mark.parametrize('input_list, nunmber, expected_result', [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [4, 6, 8]),
    ([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2, [-8, 26]),
    ([6, -25, 3, 7, 5, 5, 7, -3, 23], 1, [6]),
])
def test_get_last_n_even_numbers_returns_a_list_of_the_last_n_numbers_from_input_list(input_list, nunmber, expected_result):
    result = get_last_n_even_numbers(input_list, nunmber)
    assert result == expected_result