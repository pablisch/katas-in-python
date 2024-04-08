from lib.dna_reverse_complement import *
import pytest

@pytest.mark.parametrize('dna_string, expected_result', [
    ("TTCCGGAK", "Invalid sequence"),
    ("TTCCGGAA", "TTCCGGAA"),
    ("GACTGACTGTA","TACAGTCAGTC"),
    ("", ""),
    ("T", "A"),
    ("TC", "GA"),
    ("T T", "Invalid sequence"),
])
def test_dna_reverse_complement_returns_dna_reverse_complement_string(dna_string, expected_result):
    result = dna_reverse_complement_post_answer_my_best_option(dna_string)
    assert result == expected_result