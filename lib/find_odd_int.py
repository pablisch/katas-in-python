# https://www.codewars.com/kata/54da5a58ea159efa38000836/python
# ref: functions/make_count_dictionary.py
# KEYWORDS: odd, count, dictionary

def find_odd_int(lst):
    count_dict = {}
    for num in lst:
        count_dict[num] = count_dict.get(num, 0) + 1
    print(count_dict)
    for key, value in count_dict.items():
        if value % 2 == 1: return key

from collections import Counter

def find_odd_int_counter(lst):
    count_dict = Counter(lst)
    for key, value in count_dict.items():
        if value % 2 == 1: return key

# a better solution loops through the ints until it finds an odd count. Performance varies between solutions dependent on input.
def find_odd_int_iter_count(lst):
    for num in lst:
        if lst.count(num) % 2 == 1: return num



find_odd_int([1,1,2,-2,5,2,4,4,-1,-2,5])