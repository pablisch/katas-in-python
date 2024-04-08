def powers_of_2(n):
    powers = []
    i = 0
    while i <= n:
        powers.append(2 ** i)
        i += 1

    return powers

# this syntax is unknown to me but fairly understandble
# range is e.g. n = 3, 0 to 4 exclusive, i.e. 0 to 3 inclusive
# so the start is 2 ** x where x is each number in the range in turn
def powers_of_two(n):
    return [2**x for x in range(n+1)]

# this version is quite like mine but acknowledges that the range is known and so uses a for loop
# the range is e.g. n = 3, 0 to 4 exclusive
def powers_of_two_2(n):
    a = []
    for i in range(0, n + 1):
        a.append(2 ** i)    
    return a

print('')

# 👇🏻 experiments with the line 14 syntax
squares = [x ** 2 for x in range(1, 6)]
loves = ['I love ' + x for x in ['cheese', 'sleep', 'mountains']]
letters = [f'letter: {x.upper()}' for x in 'word']

print (squares) # => [1, 4, 9, 16, 25]
print (loves) # => ['I love cheese', 'I love sleep', 'I love mountains']
print (letters) # => ['letter: W', 'letter: O', 'letter: R', 'letter: D']
    
