import pytest
from lib.validate_username import validate_username

@pytest.mark.parametrize('username, expected_result', [
('username', True),
('1234', True),
('123', False),
('1234567890123456', True),
('12345678901234567', False),
('user_1234', True),
('username*', False),
('user-name', False),
('Username*', False),
])
def test__returns(username, expected_result):
    result = validate_username(username)
    assert result == expected_result