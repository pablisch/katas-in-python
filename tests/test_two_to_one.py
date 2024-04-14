import pytest
from lib.two_to_one import two_to_one

@pytest.mark.parametrize('s1, s2, expected_result', [
("xyaabbbccccdefww", "xxxxyyyyabklmopq", "abcdefklmopqwxy"),
("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz")
])
def test__returns(s1, s2, expected_result):
    result = two_to_one(s1, s2)
    assert result == expected_result