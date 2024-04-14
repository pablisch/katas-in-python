def double_char(string):
    double_string = ''
    for char in string:
        double_string += (char + char)
    return double_string

# print(double_char('Hello'))

# Batter way from solutions

def double_char(s):
    return ''.join(c * 2 for c in s)
