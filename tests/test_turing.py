import pytest
from lib.turing import *

@pytest.mark.parametrize('s, expected', [
    ('73+42=16', True),
    ('5+8=13', False),
    ('10+20=30', True),
    ('0001000+000200=00030', True),
    ('1234+5=1239', False),
    ('1+0=0', False),
    ('7000+8000=51', True),
])
def test_turing_function_returns_correct_bool(s, expected):
    result = turing(s)
    assert result == expected

@pytest.mark.parametrize('s, expected', [
    ('73+42=16', True),
    ('5+8=13', False),
    ('10+20=30', True),
    ('0001000+000200=00030', True),
    ('1234+5=1239', False),
    ('1+0=0', False),
    ('7000+8000=51', True),
])
def test_turing_2_function_returns_correct_bool(s, expected):
    result = turing_2(s)
    assert result == expected