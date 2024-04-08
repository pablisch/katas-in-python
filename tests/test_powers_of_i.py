import pytest
from lib.powers_of_i import pofi

@pytest.mark.parametrize('n, expected_result', [
    (0, '1'),
    (1, 'i'),
    (2, '-1'),
    (3, '-i'),
    (4, '1'),
    (5, 'i'),
    (6, '-1'),
    (7, '-i'),
    (8, '1'),
    (9, 'i'),
    (10, '-1'),
    (11, '-i'),
])
def test_pofi_returns_answer(n, expected_result):
    result = pofi(n)
    assert result == expected_result