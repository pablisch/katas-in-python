def add_length(str):
    # split the string into words
    words = str.split()
    # a list is created where the words list is mapped and the lambda applied to each word
    # the lambda makes a string interpolation with the word, a space and the length of the word
    return list(map(lambda word: f'{word} {len(word)}', words))

print (add_length("apple ban"))

# FORMAT() is definitely something worth learning more about!
# The example below clearly shows the format, or at least, a simple use case.
# Surrounding the iterated loop in square brackets creates a list
def add_length_with_format(str):
    words = str.split()
    return ["{} {}".format(word, len(word)) for word in words]

print (add_length_with_format("apple ban"))

# Probably the simplest to read, return THIS for ITEM in LOOP
def add_length_simple(str):
    words = str.split()
    return [f"{word} {len(word)}" for word in words]

print (add_length_simple("apple ban"))

# As above in a single line
def add_length_simple_one_line(str):
    return [f"{word} {len(word)}" for word in str.split()]

print (add_length_simple_one_line("apple ban"))

# A different example of for loop
def add_length_for_alternative(str):
    words = str.split()
    answer = []
    for word in words:
        answer.append(f"{word} {len(word)}")
    return answer

print (add_length_for_alternative("apple ban"))

# Probably the simplest to read, return THIS for ITEM in LOOP
def add_length_format_specifiers(str):
    words = str.split()
    return ["%s %d" % (word, len(word)) for word in words]

print (add_length_format_specifiers("apple ban"))
