import pytest
from lib.pyramids import pyramids

@pytest.mark.parametrize('n, expected_result', [
    (2,  " /\\\n/__\\\n"),
    (4,  "   /\\\n  /  \\\n /    \\\n/______\\\n"),
    (6,  "     /\\\n    /  \\\n   /    \\\n  /      \\\n /        \\\n/__________\\\n"),
    (10,  "         /\\\n        /  \\\n       /    \\\n      /      \\\n     /        \\\n    /          \\\n   /            \\\n  /              \\\n /                \\\n/__________________\\\n"),
])
def test_pyramids_returns_string_that_produces_a_pyramid_with_n_floors(n, expected_result):
    result = pyramids(n)
    assert result == expected_result