import pytest
from lib.vector_mapping import map_vector

@pytest.mark.parametrize('vector, circle1, circle2, expected_result', [
    ((46, 58), (0, 0, 100), (0, 0, 100), (46, 58)),
    ((5, 5), (10, 20, 42), (-100, -42, 60), (-107.14, -63.43)),
    ((120, 58), (100, 76, 36), (120, -62, 50), (147.78, -87.0))
])
def test_map_vector_returns_end_coords(vector, circle1, circle2, expected_result):
    result = map_vector(vector, circle1, circle2)
    assert result == expected_result