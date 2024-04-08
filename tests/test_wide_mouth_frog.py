from lib.wide_mouth_frog import get_mouth_size
import pytest

@pytest.mark.parametrize("animal", ["lion", "crocodile", "aligator", "teapot"])
def test_returns_wide_mouth_size_when_not_passed_alligator(animal):
  result = get_mouth_size(animal)
  assert result == "wide"

def test_returns_narrow_when_passed_alligator():
  result = get_mouth_size("alligator")
  assert result == "small"