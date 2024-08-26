# https://www.codewars.com/kata/53697be005f803751e0015aa/python
# Replaces keys with values in dictionary.
# KEYWORDS: translate, substitute, replace, switch, encode, decode, maketrans

# My first basic approach. It works pretty well and is quite readable
vowels = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
numbers = {value: key for key, value in vowels.items()}

def encode(string):
    for key, value in vowels.items():
        string = string.replace(key, value)
    return string

def decode(string):
    for key, value in numbers.items():
        string = string.replace(key, value)
    return string

# Approach two using the str.translate() method.
# translate_vowels = str.maketrans(vowels) # vowels is defined on line 6
translate_vowels = str.maketrans('aeiou', '12345')

def encode_with_translate(string):
    return string.translate(translate_vowels)

translate_numbers = str.maketrans('12345', 'aeiou')

def decode_with_translate(string):
    return string.translate(translate_numbers)

print (decode_with_translate("h2llo"))