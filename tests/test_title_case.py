import pytest
from lib.title_case import *

@pytest.mark.parametrize('s1, s2, expected', [
    ('a clash of KINGS', 'a an the of', 'A Clash of Kings'),
    ('THE WIND IN THE WILLOWS', 'The In', 'The Wind in the Willows'),
])
def test_title_case_should_return_the_correct_title_casing(s1, s2, expected):
    result = title_case(s1, s2)
    assert result == expected

@pytest.mark.parametrize('s1, s2, expected', [
    ('a clash of KINGS', 'a an the of', 'A Clash of Kings'),
    ('THE WIND IN THE WILLOWS', 'The In', 'The Wind in the Willows'),
    ('THE WIND IN THE WILLOWS', 'Then Inn', 'The Wind In The Willows'),
])
def test_title_case_cw_1_should_return_the_correct_title_casing(s1, s2, expected):
    result = title_case_cw_1(s1, s2)
    assert result == expected