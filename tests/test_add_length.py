import pytest
from lib.add_length import add_length

@pytest.mark.parametrize('string, expected_result', [
    ("apple ban", ["apple 5", "ban 3"]),
    ("you will win", ["you 3", "will 4", "win 3"]),
])
def test_add_length_function_returns_correct_list(string, expected_result):
    result = add_length(string)
    assert result == expected_result

def test_add_length_single_test():
    result = add_length("single case test")
    expected_result = ["single 6", "case 4", "test 4"]
    assert result == expected_result