import re

def is_letter(string):
    return bool(re.search("^[a-zA-Z]$", string))

my_string = 'I went to see and I saw.'
x = re.sub("I", "you", my_string)
print(x) # => 'you went to see and you saw.'

my_string = 'I went to see and I saw.'
x = re.sub("I", "you", my_string, 1)
print(x) # => 'you went to see and I saw.'