from lib.multiples import get_multiples
import pytest

@pytest.mark.parametrize("num, limit, expected_result", [
  (2, 6, [2, 4, 6]),
  (3, 6, [3, 6]),
  (3, 5, [3]),
  (10, 55, [10, 20, 30, 40, 50]),
  ])
def test_returns_array_of_multiples_of_number_up_to_limit(num, limit, expected_result):
  result = get_multiples(num, limit)
  assert result == expected_result
