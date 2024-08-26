import pytest
from lib.data_reverse import data_reverse

@pytest.mark.parametrize('list_, expected_result', [
    ([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0], [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]),
    ([0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1], [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]),
])
def test_data_reverse_function_returns_correctly_amended_data(list_, expected_result):
    result = data_reverse(list_)
    assert result == expected_result