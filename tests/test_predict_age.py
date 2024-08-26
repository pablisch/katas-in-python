import pytest
from lib.predict_age import *

@pytest.mark.parametrize('age1, age2, age3, age4, age5, age6, age7, age8, expected_result', [
    (65, 60, 75, 55, 60, 63, 64, 45, 86),
])
def test_predict_age_function_returns_expected_age(age1, age2, age3, age4, age5, age6, age7, age8, expected_result):
    result = predict_age(age1, age2, age3, age4, age5, age6, age7, age8)
    assert result == expected_result

@pytest.mark.parametrize('age1, age2, age3, age4, age5, age6, age7, age8, expected_result', [
    (65, 60, 75, 55, 60, 63, 64, 45, 86),
])
def test_predict_age_concise_function_returns_expected_age(age1, age2, age3, age4, age5, age6, age7, age8, expected_result):
    result = predict_age_concise(age1, age2, age3, age4, age5, age6, age7, age8)
    assert result == expected_result