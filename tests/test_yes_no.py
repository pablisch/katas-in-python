import pytest
from lib.yes_no import yes_no

@pytest.mark.parametrize('input_data, expected_result', [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [ 1, 3, 5, 7, 9, 2, 6, 10, 8, 4 ]),
    (['this', 'code', 'is', 'right', 'the'], [ 'this', 'is', 'the', 'right', 'code' ]),
    (["a"], ["a"]),
    (["a", "b"], ["a", "b"]),
    ([], []),
    (['beware', 666, 'mighty', 42, 'pippi', 'pippi', 'testing', 5, '!', 42, 'testing', 42, 'cat', 'you', 666], ['beware', 'mighty', 'pippi', 'testing', '!', 'testing', 'cat', 666, 42, 5, 42, 666, 42, 'pippi', 'you']),
])
def test_yes_no_returns_array_of_first_out_first_in_elements(input_data, expected_result):
    result = yes_no(input_data)
    assert result == expected_result