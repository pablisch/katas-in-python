# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/solutions/python
# KEYWORDS: nested_list, sum, minimum, for, map

def sum_of_minimums(lst):
    return sum(min(arr) for arr in lst)

# Adjusting to Python syntax, map takes in a function and an iterable, so here, .min() applies to each el of numbers.
def sum_of_minimums_cw(numbers):
    return sum(map(min, numbers))

list_ = [[1,4],[2,6], [6,8]]

sum_of_minimums(list_)