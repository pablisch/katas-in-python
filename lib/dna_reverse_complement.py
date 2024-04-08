import re

def dna_reverse_complement(dna):
    reverse_dna = dna[::-1].upper()
    if bool(re.search("[^TGAC]", reverse_dna)) == True:
        return "Invalid sequence"
    swap_map = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    dna_reverse_complement_list = (swap_map[char] for char in reverse_dna)
    dna_reverse_complement = "".join(dna_reverse_complement_list)
    return dna_reverse_complement

def dna_reverse_complement_refactor(dna):
    reverse_dna = dna[::-1].upper()
    if bool(re.search("[^TGAC]", reverse_dna)) == True:
        return "Invalid sequence"
    swap_map = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    return "".join(swap_map[char] for char in reverse_dna)

# This is not the most concise but is a compromise of readability and brevity, plus uses no packages
def dna_reverse_complement_post_answer_my_best_option(dna):
    swap_pairs = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    dna = dna[::-1].upper()
    return "Invalid sequence" if not set(dna).issubset({'A', 'T', 'C', 'G', ''}) else "".join(swap_pairs[char] for char in dna)

# This uses regex rather than set and subset
def dna_reverse_complement_post_answer_2(dna):
    swap_pairs = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    dna = dna[::-1].upper()
    return "Invalid sequence" if bool(re.search("[^TGAC]", dna)) == True else "".join(swap_pairs[char] for char in dna)





