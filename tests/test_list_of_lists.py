import pytest
from lib.list_of_lists import process_data

@pytest.mark.parametrize('list, expected_result', [
    ([[2, 5], [3, 4], [8, 7]], 3),
    ([[2, 5], [3, 4], [8, 8]], 0),
])
def test_process_data_returns_the_product_of_the_sum_of_each_sublist(list, expected_result):
    result = process_data(list)
    assert result == expected_result