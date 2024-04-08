def validate_word(word):
    count = {}

    for char in word:
        char = char.lower()
        count[char] = count.get(char, 0) + 1

    print(count)

    return min(count.values()) == max(count.values())

# codewars top solution - requires package
from collections import Counter

def validate_word1(word):
    return len(set(Counter(word.lower()).values())) == 1

# codewars 2nd top solution
def validate_word2(word):
    word = word.lower()
    return len(set(word.count(char) for char in word)) == 1

