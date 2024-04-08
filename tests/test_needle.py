from lib.needle import find_needle
import pytest

@pytest.mark.parametrize('haystack, expected_result', [
    (["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"], "found the needle at position 5"),
    (['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago'], 'found the needle at position 5'),
    ([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54], 'found the needle at position 30'),
])
def test_find_needle_returns_a_string_containing_index_of_needle(haystack, expected_result):
    result = find_needle(haystack)
    assert result == expected_result



