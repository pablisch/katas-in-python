# KEYWORDS: logical operators, isinstance, in, not, symbols, maths_operators, interpolation, type, chaining, chained_operators

def calculator(num1, num2, op):
    if not isinstance(num1, int) or not isinstance(num2, int) or not isinstance(op, str) or op not in "+-*/": return "unknown value"
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif num2 == 0:
        return "undefined"
    elif op == "/":
        return num1 / num2

# This is a far better solution in every way except that it does not account for division by zero
def calculator_cw(x, y, op):
  return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'

# eval evaluates the expression in parentheses. I was not sure how it would handle the strings of operations but it works fine.
# the chained equality works really well in place of individually checking that x and y are ints,'type(x) == type(y) == int'
# str(op) in '+-*/' checks the op is a valid sign and handles if it is not a string
# else handles any other case



q = "undefined"
w = 1
e = "*"
print (eval(f'{q}{e}{w}', {q: 20, w: 3, e: '-'}, {q: 40, w: 20, e: '-'}))
# print (eval(f'{q}{e}{w}'))
