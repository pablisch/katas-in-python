import pytest
from lib.tabs_to_spaces import tabs_to_spaces

@pytest.mark.parametrize('input, expected_result', [
    ("ab\t12","ab  12"),
    ("a\t123\n\t123","a   123\n    123"),
    ("a\tbcdef\t1\t23456\nab\tcdef\t123 456\n\tabcdef\t12\t3456\na\tbcdef\t\t12346","a   bcdef   1   23456\nab  cdef    123 456\n    abcdef  12  3456\na   bcdef       12346"),
])
def test_tabs_to_spaces_returns_string_with_tabs_replaced_with_spaces(input, expected_result):
    result = tabs_to_spaces(input)
    assert result == expected_result