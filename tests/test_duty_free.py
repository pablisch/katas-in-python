from lib.duty_free import *
import pytest

@pytest.mark.parametrize('normal_price, discount, holiday_price, expected_result', [
  (10, 10, 500, 500),
  (12, 50, 1000, 166),
])
def test_returns_bottles_needed_to_pay_for_holiday(normal_price, discount, holiday_price, expected_result):
  result = calculate_bottle_savings(normal_price, discount, holiday_price)
  assert result == expected_result