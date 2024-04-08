from lib.welcome_to import welcome_to
import pytest

@pytest.mark.parametrize('name_array, city, state, expected_string', [
    (['John', 'Smith'], 'Phoenix', 'Arizona', 'Hello, John Smith! Welcome to Phoenix, Arizona!'),
    (['Jane', 'Alice', 'Smith'], 'Paris', 'Texas', 'Hello, Jane Alice Smith! Welcome to Paris, Texas!'),
])
def test_welcome_to_returns_welcome_string(name_array, city, state, expected_string):
    result = welcome_to(name_array, city, state)
    assert result == expected_string

