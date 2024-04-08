from functions.replacement_mapping import *
import pytest

# Test for ALL chars in a STRING
@pytest.mark.parametrize('string, replacement_map, expected_result', [
    ('hello', {'h': 'm', 'e': 'a', 'l': 't', 'o': 'i'}, 'matti'),
    ('hello', {'h': 'H', 'e': '3', 'l': '1', 'o': '0'}, 'H3110'),
])
def test_replace_all_chars_in_string_returns_string_with_mapped_replacements(string, replacement_map, expected_result):
    result = replace_all_chars_in_string(string, replacement_map)
    assert result == expected_result

# Test for ALL items in a LIST
@pytest.mark.parametrize('list, replacement_map, expected_result', [
    (['h', 'e', 'l', 'l'], {'h': 'm', 'e': 'a', 'l': 't', 'o': 'i'}, ['m', 'a', 't', 't']),
    (['hole', 2, True, 'thing'], {'hole': 'mole', 2: 13, True: False, 'thing': 1000}, ['mole', 13, False, 1000]),
    # (('hole', 1, 'thing'), {'hole': 'mole', 1: 13, 'thing': 1000}, ('mole', 13, 1000)), # For Tuple
    # ({'hole', 1, 'thing'}, {'hole': 'mole', 1: 13, 'thing': 1000}, {'mole', 13, 1000}), # For Set
])
def test_replace_all_items_in_list_returns_list_with_mapped_replacements(list, replacement_map, expected_result):
    result = replace_all_items_in_list(list, replacement_map)
    assert result == expected_result

# Test for SELECTED chars in a STRING
@pytest.mark.parametrize('string, replacement_map, expected_result', [
    ('hello', {'h': 'm', 'e': 'a', 'l': 't', 'o': 'i'}, 'matti'),
    ('hellorty', {'h': 'H', 'e': '3', 'l': '1', 'o': '0'}, 'H3110rty'),
    ('querty', {'h': 'H', 'e': '3', 'l': '1', 'o': '0'}, 'qu3rty'),
    ('quirty', {'h': 'H', 'e': '3', 'l': '1', 'o': '0'}, 'quirty'),
])
def test_replace_selected_chars_in_string_returns_string_with_mapped_replacements(string, replacement_map, expected_result):
    result =  replace_selected_chars_in_string(string, replacement_map)
    assert result == expected_result

# Test for SELECTED items in a LIST
@pytest.mark.parametrize('iterable, replacement_map, expected_result', [
    (['h', 'e', 'l', 'l'], {'h': 'm', 'e': 'a', 'l': 't', 'o': 'i'}, ['m', 'a', 't', 't']),
    (['h', 'e', 'l', 'l', 'o'], {'h': 'm', 'e': 'a', 'l': 't', 'u': 'i'}, ['m', 'a', 't', 't', 'o']),
    (['help', 7, True], {'help': 'me', True: False, 7: 13}, ['me', 13, False]),
])
def test_replace_selected_items_in_list_returns_list_with_mapped_replacements(iterable, replacement_map, expected_result):
    result = replace_selected_items_in_list(iterable, replacement_map)
    assert result == expected_result

# Test for SELECTED items in a TUPLE
@pytest.mark.parametrize('iterable, replacement_map, expected_result', [
    (('h', 'e', 'l', 'l'), {'h': 'm', 'e': 'a', 'l': 't', 'o': 'i'}, ('m', 'a', 't', 't')),
    (('h', 'e', 'l', 'l', 'o'), {'h': 'm', 'e': 'a', 'l': 't', 'u': 'i'}, ('m', 'a', 't', 't', 'o')),
    (('help', 7, True), {'help': 'me', True: False, 7: 13}, ('me', 13, False)),
])
def test_replace_selected_items_in_tuple_returns_tuple_with_mapped_replacements(iterable, replacement_map, expected_result):
    result = replace_selected_items_in_tuple(iterable, replacement_map)
    assert result == expected_result

# Test for SELECTED items in a SET
@pytest.mark.parametrize('iterable, replacement_map, expected_result', [
    ({'h', 'e', 'l', 'l'}, {'h': 'm', 'e': 'a', 'l': 't', 'o': 'i'}, {'m', 'a', 't', 't'}),
    ({'h', 'e', 'l', 'l', 'o'}, {'h': 'm', 'e': 'a', 'l': 't', 'u': 'i'}, {'m', 'a', 't', 't', 'o'}),
    ({'help', 7, True}, {'help': 'me', True: False, 7: 13}, {'me', 13, False}),
])
def test_replace_selected_items_in_set_returns_set_with_mapped_replacements(iterable, replacement_map, expected_result):
    result = replace_selected_items_in_set(iterable, replacement_map)
    assert result == expected_result