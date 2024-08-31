# KEYWORDS: filter, lambda, isalpha, letter, alphabet, filter_string, string, reverse, reversed, regex

def reverse(str_):
    return "".join(list(filter(lambda char: char.isalpha(), str_[::-1])))

# a simpler way - [i for i in str_  ...  if i.isalpha()]
def reverse_cw_1(str_):
    return ''.join([i for i in str_ if i.isalpha()])[::-1]

# no list/array - did not know you could filter a string! the filter produces a filter object which is then joined
# str is Python string representing each string char in the reversed string
def reverse_cw_2(str_):
    return ''.join(filter(str.isalpha, reversed(str_)))

# love a bit of regex! Nice to see the ^ everything except operator
import re
def reverse_letter_regex(string):
    return re.sub("[^a-zA-Z]","",string)[::-1]

print (filter(str == "t", "tight t shirt")) # => <filter object at 0x109e720e0>
