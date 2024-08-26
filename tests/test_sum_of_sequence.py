import pytest
from lib.sum_of_sequence import *

@pytest.mark.parametrize('begin_number, end_number, step, expected_result', [
    (2, 6, 2, 12),
    (2, 2, 1, 2),
    (2, 24, 22, 26),
    (16, 15, 3, 0),
])
def test_sum_of_sequence_function_returns_correct_sum(begin_number, end_number, step, expected_result):
    result = sequence_sum(begin_number, end_number, step)
    assert result == expected_result