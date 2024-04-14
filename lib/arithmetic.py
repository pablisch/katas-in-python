import operator

def arithmetic(a, b, op):
    operators = {'add': operator.add, 'subtract': operator.sub, 'multiply': operator.mul, 'divide': operator.truediv}
    return operators[op](a, b)

# There was a far more obvious way of doing this:
def arithmetic(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]

# This is how I did it but far better written:
from operator import add, mul, sub, truediv


def arithmetic(a, b, operator):
    ops = {'add': add, 'subtract': sub, 'multiply': mul, 'divide': truediv}
    return ops[operator](a, b)