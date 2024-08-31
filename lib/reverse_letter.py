# KEYWORDS: filter, lambda, isalpha, letter, alphabet, filter_string, string, reverse, reversed

def reverse(str_):
    return "".join(list(filter(lambda char: char.isalpha(), str_[::-1])))

# a simpler way - [i for i in str_  ...  if i.isalpha()]
def reverse_cw_1(str_):
    return ''.join([i for i in str_ if i.isalpha()])[::-1]

# no list/array - did not know you could filter a string! the filter produces a filter object which is then joined
# str is Python string representing each string char in the reversed string
def reverse_cw_2(str_):
    return ''.join(filter(str.isalpha, reversed(str_)))

print (filter(str == "t", "tight t shirt")) # => <filter object at 0x109e720e0>
