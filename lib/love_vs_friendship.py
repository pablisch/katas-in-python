def get_alphabet_value(char):
    return ord(char) - 96

def get_word_value_1(word):
    return sum(map(lambda char: ord(char) - 96, word))
# 👆🏻 the lambda is the same as the function, get_alphabet_value, above. Adds together the values of the chars in word

def get_word_value(word):
    values = [ord(char) - 96 for char in word] # ord(<char>) returns the ascii value, e.g. 'a' == 97, so ord(char)-96 returns 1 for 'a',... 26 for 'z'. This line creates an array of values in the given word.
    return sum(values) # returns the sum of the values



    