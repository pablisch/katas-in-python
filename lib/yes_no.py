def yes_no_1(arr):
    print('starting')
    target = len(arr)
    results = []
    zero_start = True
    while len(results) < target:
        spare = []
        # print('len:', len(arr), 'arr:', arr)
        if zero_start:
            for index, x in enumerate(arr): 
                results.append(x) if not index % 2 else spare.append(x)
        else:
            for index, x in enumerate(arr):
                results.append(x) if index % 2 else spare.append(x)
        
        zero_start = False if len(arr) % 2 else True
        arr = spare[:]
        print('results:', results, 'spares:', arr, 'start at 0:', zero_start)

    print('results:', results, 'new arr:', arr, 'start at 0:', zero_start)

    return results

def yes_no_2(arr):
    results = []
    zero_start = True
    while len(arr) > 0:
        spare = []
        if zero_start:
            for index, x in enumerate(arr): 
                results.append(x) if not index % 2 else spare.append(x)
        else:
            for index, x in enumerate(arr):
                results.append(x) if index % 2 else spare.append(x)
        
        zero_start = False if (len(arr) % 2 and zero_start) or (not len(arr) % 2 and not zero_start) == True else True
        arr = spare[:]
        print('results:', results)
        print('spares:', arr, 'start at 0:', zero_start)

    print('results:', results, 'new arr:', arr, 'start at 0:', zero_start)

    return results

# I was really a bit clueless about a good way to achieve this. I used a logical way within my slender knowledge of python but can learn from the approaches of others

# codewars solutions:

# deque (double-ended queue) is an efficient way to deal with operation at both ends of a list
from collections import deque

def yes_no_deque(arr):
    d = deque(arr) # creates a deque object from arr (double-ended queue)
    result = []
    while d: # while d (deque object) is not empty
        result.append(d.popleft()) # append result with the leftmost element of d
        d.rotate(-1) # shift d left by one position, i.e. the leftmost el goes to the end
    return result

# All of these solutions appear to use this same system that I did npt realise, that alternating taking an item and sending the next to the back of the list achieves everything I did in a far more complex and difficult way.
def yes_no_pop(arr):
    result = []
    while arr: # presumably while arr has any elements
        result.append(arr.pop(0)) # this item to results
        if arr:
            arr.append(arr.pop(0)) # this item to the end of arr
    return result

def yes_no(arr):
    result, i = [], 0 # initialise results list and i = 0
    while arr:
        result.extend(arr[i::2]) # adds arr els from index i to the end in steps of 2, i.e. every other el. i starts at 0.
        j = i != len(arr) % 2 # j = 1 if (i = 1 and the length of arr is even) OR (i = 0 and the length of arr is odd) BUT j = 0 if (i = 0 and the length of arr is even) OR (i = 1 and the length of arr is odd). This is used to say which els in arr get put into results, odd or even indexes.
        arr = arr[1-i::2] # reassigning arr for the next loop. 1 - i is either 0 or 1 depending on i. Runs to the end of the array in steps of 2. This is everything that was not put in results.
        i = j # sets i for the next round.
    return result