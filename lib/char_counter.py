from collections import Counter

phrase = 'Hello, World!'
count_object = Counter(phrase.lower())
print(count_object) # => Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})
print(count_object.values()) # => dict_values([1, 1, 3, 2, 1, 1, 1, 1, 1, 1])
print(list(count_object)) # => ['h', 'e', 'l', 'o', ',', ' ', 'w', 'r', 'd', '!']
print(list(count_object.items())) # => [('h', 1), ('e', 1), ('l', 3), ('o', 2), (',', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1), ('!', 1)]

def validate_word(word):
    return len(set(Counter(word.lower()).values())) == 1

def validate_word_clear(word):
    word = word.lower()
    count_object = Counter(word)
    count_values = count_object.values()
    unique_count_values = set(count_values)

    return len(unique_count_values) == 1