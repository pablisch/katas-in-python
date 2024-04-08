from lib.hero_survival import will_they_survive
import pytest

@pytest.mark.parametrize('bullets, dragons, expected_result', [
    (10, 5, True),
    (100, 40, True),
    (7, 4, False),
    (4, 5, False),
    (1500, 751, False),
    (0, 1, False),
])
def test_returns_result_given_bullets_and_dragon_values(bullets, dragons, expected_result):
    result = will_they_survive(bullets, dragons)
    assert result == expected_result