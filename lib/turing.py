# https://www.codewars.com/kata/5a1e6323ffe75f71ae000026/train/python
# KEYWORDS: multi_split, int, reverse, map, lambda, replace, tuple

def turing(s):
    numbers_1 = s.split('+')
    numbers_2 = numbers_1[1].split('=')
    numbers = [numbers_1[0], numbers_2[0], numbers_2[1]]
    reversed_numbers = list(map(lambda x: int(str(x)[::-1]), numbers))
    return (reversed_numbers[0] + reversed_numbers[1] == reversed_numbers[2])

def turing_2(s):
    num1, num2, num3 = s.replace('+', '=').split('=')
    reversed_numbers = [int(str(x)[::-1]) for x in (num1, num2, num3)]
    return reversed_numbers[0] + reversed_numbers[1] == reversed_numbers[2]

# of course regex makes everything more simple
import re
def is_turing_equation(s):
    a, b, c = (int(n[::-1]) for n in re.split('[+=]', s))
    return a + b == c


turing('73+42=16')