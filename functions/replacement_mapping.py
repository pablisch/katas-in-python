# SEE tests/test_replacement_mapping.py for tests
# Use a dictionary to replace items in an iterable such as a string, tuple or list BUT NOT dictionaries
# Apart from easy replacement of multiple values, this also allows for swapping

# This first function will throw an error for any char in the string that is not in the replacement_map
def replace_all_chars_in_string(string, replacement_map):
    return ''.join(replacement_map[char] for char in string)

# As above but for lists. Can be adapted for sets and tuples using their constructors
def replace_all_items_in_list(input_list, replacement_map):
    return list(replacement_map[item] for item in input_list)

# This function will return self if item is not in the replacement_map
# It does everything the first does with the extra ability to accept non-mapped items
def replace_selected_chars_in_string(string, replacement_map):
    return ''.join(replacement_map.get(char, char) for char in string)

# As above but for lists.
def replace_selected_items_in_list(input_list, replacement_map):
    return list(replacement_map.get(item, item) for item in input_list)

# As above but for tuple.
def replace_selected_items_in_tuple(input_tuple, replacement_map):
    return tuple(replacement_map.get(item, item) for item in input_tuple)

# As above but for set.
def replace_selected_items_in_set(input_set, replacement_map):
    return set(replacement_map.get(item, item) for item in input_set)

# Example Test:
import pytest
# Test for ALL chars in a STRING
@pytest.mark.parametrize('string, replacement_map, expected_result', [
    ('hello', {'h': 'm', 'e': 'a', 'l': 't', 'o': 'i'}, 'matti'),
    ('hello', {'h': 'H', 'e': '3', 'l': '1', 'o': '0'}, 'H3110'),
])
def test_replace_all_chars_in_string_returns_string_with_mapped_replacements(string, replacement_map, expected_result):
    result = replace_all_chars_in_string(string, replacement_map)
    assert result == expected_result
