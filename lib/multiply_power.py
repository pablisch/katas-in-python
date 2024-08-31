# https://www.codewars.com/kata/5708f682c69b48047b000e07/python
# KEYWORDS: power, maths,

def multiply_power(n):
    return n * 5 ** len(str(abs(n)))