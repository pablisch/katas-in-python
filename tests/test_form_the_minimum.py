import pytest
from lib.form_the_minimum import form_the_minimum

@pytest.mark.parametrize('list, expected_result', [
    ({1, 3, 1}, 13),
    ({1, 9, 3, 1, 7, 4, 6, 6, 7}, 134679),
])
def test_form_the_minimum_returns_smallest_number_from_unique_digits(list, expected_result):
    result = form_the_minimum(list)
    assert result == expected_result