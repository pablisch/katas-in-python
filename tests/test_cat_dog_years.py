from lib.cat_dog_years import owned_cat_and_dog
import pytest

@pytest.mark.parametrize('cat_years, dog_years, expected_result', [
    (9, 7, [0, 0]),
    (15, 15, [1, 1]),
    (56, 64, [10, 10]),
])
def test_owned_cat_and_dog_returns_array_of_how_long_pets_have_been_owned(cat_years, dog_years, expected_result):
    result = owned_cat_and_dog(cat_years, dog_years)
    assert result == expected_result