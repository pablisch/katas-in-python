import math

def calculate_bottle_savings2(normal_price, discount, holiday_price):
  savings_per_bottle = normal_price * discount / 100
  bottles_to_pay_for_holiday = holiday_price / savings_per_bottle
  return math.floor(bottles_to_pay_for_holiday)

def calculate_bottle_savings(normal_price, discount, holiday_price):
  savings_per_bottle = normal_price * discount / 100
  bottles_to_pay_for_holiday = holiday_price // savings_per_bottle
  return bottles_to_pay_for_holiday