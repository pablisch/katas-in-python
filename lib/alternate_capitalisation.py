def alternate_capitalisation(string):
    result_array = ['', '']
    for char in string:
        if len(result_array[0]) % 2 == 0:
            result_array[0] += char.upper()
            result_array[1] += char.lower()
        else:
            result_array[1] += char.upper()
            result_array[0] += char.lower()
            
    return result_array

# Codewars post-submission solutions
def capitalize1(string):
    # enumerate(string) creates an enumerate object from the string, e.g. (0, 's'), (1, 't'), (2, 'r'), (3, 'i'), (4, 'n'), (5, 'g') except as an enumerator.
    # the for loop iterates over each index and char in the enumerator object
    # the beginning of the expression is a ternary operator:
    # char if index % 2 means, if index % 2 returns any value other than 0, then return char (lowercase)
    # anything else, i.e. index % 2 is 0 (false) then return char.upper(), so the first char is uppercase
    # in other words, uppercase then lowercase then uppercase, etc.
    # the very beginning is join without spaces.
    string = ''.join(char if index % 2 else char.upper() for index, char in enumerate(string))
    # the return is an array with the created string and the swapcase version of it
    return [string, string.swapcase()]

def capitalize2(s):
    result = ['',''] # as I did, create the result array and concatenate onto the empty strings
    for i,c in enumerate(s): # creates an enumerator object as described above
        result[0] += c.lower() if i % 2 else c.upper() # add lower char for odd index, else upper
        result[1] += c.upper() if i % 2 else c.lower() # add upper char for odd index, else lower
    return result

# A simple revision of my original using swapcase()
def alternate_capitalisation_swap(string):
    first_string = ''
    for char in string:
        first_string += char.upper() if len(first_string) % 2 == 0 else char.lower()
            
    return [first_string, first_string.swapcase()]

