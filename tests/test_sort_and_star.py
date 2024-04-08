from lib.sort_and_star import sort_and_star
import pytest

@pytest.mark.parametrize('input_array, expected_result', [
    (["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"], 'b***i***t***c***o***i***n'),
    (["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"], 'a***r***e'),
    (["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"], 'L***e***t***s'),
])
def test_sort_and_star_returns_first_sorted_string_with_asterisks_between_chars_when_passed_array(input_array, expected_result):
    result = sort_and_star(input_array)
    assert result == expected_result