import pytest
from lib.truncate import *

@pytest.mark.parametrize('name, expected_result', [
    ("Mexico", ["Mexico", "Me"]),
    ("Ymd", ["Ymd", "Ym"]),
    ("Me", ["Me"]),
    ("I", ["I"]),
    ("", [""]),
])
def test_truncate_function_returns_the_truncated_name_list(name, expected_result):
    result = truncate(name)
    assert result == expected_result

@pytest.mark.parametrize('name, expected_result', [
    ("Mexico", ["Mexico", "Me"]),
    ("Ymd", ["Ymd", "Ym"]),
    ("Me", ["Me"]),
    ("I", ["I"]),
    ("", [""]),
])
def test_who_is_paying_function_returns_the_truncated_name_list(name, expected_result):
    result = who_is_paying_cw_1(name)
    assert result == expected_result