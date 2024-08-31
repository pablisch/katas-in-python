# https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/python
# KEYWORDS: truncate, string_indexing, string_range, string_split, lambda, one_line

def truncate(name):
    return [name, name[0:2]] if len(name) > 2 else [name]

# NEW TO ME... the (n) at the end calls the lambda right away. Seen a similar thing in JS.
# It is kind of weird but since the lambda is an anonymous function, the whole thing is a function that calls a function!
def who_is_paying_cw_1(n):
    return (lambda n: [n, n[:2]] if len(n) > 2 else [n])(n)

# this shows how the lambda is a function that gets called with the arg passed in, i.e. 5. It is the parentheses that call the function... the 5 is simply an arg.
print ((lambda n: n + 3)(5))

# As far as I can see, 'who_is_paying_cw_2' is a var referencing an anonymous function.
who_is_paying_cw_2 = lambda n: [n, n[:2]] if len(n)>2 else [n]

# the function is called like this, i.e. reference the func with the var with an arg.
who_is_paying_cw_2("Pablo")