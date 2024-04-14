import pytest
from lib.row_weights import row_weights

@pytest.mark.parametrize('param, expected_result', [
([13, 27, 49], (62, 27)),
([50, 60, 70, 80], (120, 140)),
])
def test__returns(param, expected_result):
    result = row_weights(param)
    assert result == expected_result

