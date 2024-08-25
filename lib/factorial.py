from functools import reduce
from operator import imul

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_with_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

def factorial_with_reduce_and_lambda(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

def factorial_with_reduce_and_imul(n):
    return reduce(imul, range(1, n + 1), 1)

# NOTE: There is a factorial function in the maths module which can be imported and used.
# from math import factorial