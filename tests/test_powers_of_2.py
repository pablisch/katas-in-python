from lib.powers_of_2 import powers_of_2
import pytest

@pytest.mark.parametrize('n, expected_result', [
    (0, [1]),
    (1, [1, 2]),
    (2, [1, 2, 4]),
    (3, [1, 2, 4, 8]),
])
def test_powers_of_2_returns_an_array_of_powers_of_2_from_0_to_n(n, expected_result):
    result = powers_of_2(n)
    assert result == expected_result