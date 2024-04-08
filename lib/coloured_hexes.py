def coloured_hexes(hex_string):
    hex_list = hex_string.split(' ')
    if len(set(hex_list)) == 1:
        return 'black' if hex_list[0] == '000' or hex_list[0] == '' else 'white'
    if len(set(hex_list)) == 2 and hex_list.count(min(hex_list)) == 1:
        return 'cyan' if min(hex_list) == hex_list[0] else 'magenta' if min(hex_list) == hex_list[1] else 'yellow'
    return 'red' if max(hex_list) == hex_list[0] else 'green' if max(hex_list) == hex_list[1] else 'blue'

# codewars solution
colors = {
    (1, 0, 0): 'red',
    (0, 1, 0): 'green',
    (0, 0, 1): 'blue',
    (1, 0, 1): 'magenta',
    (1, 1, 0): 'yellow',
    (0, 1, 1): 'cyan',
    (1, 1, 1): 'white',
}

def hex_color(codes):
    codes = codes or '0 0 0' # allows for empty string
    items = [int(c) for c in codes.split()] # create list on integers, e.g. [21, 21, 20]
    print(items)
    m = max(items) # max value, e.g. 21
    print(m)
    print(tuple(i == m for i in items))
    print(colors[tuple(i == m for i in items)])
    # The next line: tuple(i == m for i in items) creates a tuple of Booleans based on comparison with m (max_value), e.g. (True, True, False) which is equivalent to (1, 1, 0)
    # The resulting tuple is used as the key for the colors dictionary.
    # if m == 0 then 'black' is returned, else the value corresponding to the color key
    return colors[tuple(i == m for i in items)] if m else 'black'
