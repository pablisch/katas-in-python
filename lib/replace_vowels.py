import re

def replace_vowels_1(s):
    new_string = ''
    for c in s: new_string += '!' if bool(re.search("[aeiouAEIOU]", c)) else c
    return new_string

def replace_vowels(s):
    return ''.join('!' if bool(re.search("[aeiouAEIOU]", c)) else c for c in s)

# print(replace_vowels('Hi!'))
# print(replace_vowels('abcde'))

# Better options from solutions

def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)

import re

def replace_exclamation(s):
    return re.sub('[aeiouAEIOU]', '!', s)