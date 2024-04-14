import pytest
from lib.arithmetic import arithmetic

@pytest.mark.parametrize('a, b, operator_string, expected_result', [
(5, 2, "add", 7),
(5, 2, "subtract", 3),
(5, 2, "multiply", 10),
(5, 2, "divide", 2.5),
])
def test__returns(a, b, operator_string, expected_result):
    result = arithmetic(a, b, operator_string)
    assert result == expected_result