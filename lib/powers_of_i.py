def pofi_1(n):
    return '1' if n % 4 == 0 else 'i' if n % 4 == 1 else '-1' if  n % 4 == 2 else '-i'

x = {0: '1', 1: 'i', 2: '-1', 3: '-i'}

def pofi(n):
    return x[n % 4]

# codewars solutions

def pofi(n):
    return ['1','i','-1','-i'][n%4] # similar to mine but simpler. n % 4 provides the index of the array to return

def pofi(n):
    return {0:"1", 1:"i", 2:"-1", 3:"-i"}[n % 4] # same as mine but on a single line which makes more sense