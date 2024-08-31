import pytest
from lib.reverse_letter import *

@pytest.mark.parametrize('str_, expected_result', [
    ('krishan', 'nahsirk'),
    ('ultr53o?n', 'nortlu'),
])
def test_reverse_returns_reversed_sanitised_string(str_, expected_result):
    result = reverse(str_)
    assert result == expected_result

@pytest.mark.parametrize('str_, expected_result', [
    ('krishan', 'nahsirk'),
    ('ultr53o?n', 'nortlu'),
])
def test_reverse_cw_1_returns_reversed_sanitised_string(str_, expected_result):
    result = reverse_cw_1(str_)
    assert result == expected_result

@pytest.mark.parametrize('str_, expected_result', [
    ('krishan', 'nahsirk'),
    ('ultr53o?n', 'nortlu'),
])
def test_reverse_cw_2_returns_reversed_sanitised_string(str_, expected_result):
    result = reverse_cw_2(str_)
    assert result == expected_result
