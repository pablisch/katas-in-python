from lib.integers_between import integers_between
import pytest

@pytest.mark.parametrize('num1, num2, expected_result', [
    (1, 4, [1, 2, 3, 4]),
    (3, 4, [3, 4]),
    (4, 9, [4, 5, 6, 7, 8, 9]),
])
def test_integers_between_returns_an_array_of_ints_from_num1_to_num2_inclusive(num1, num2, expected_result):
    result = integers_between(num1, num2)
    assert result == expected_result


