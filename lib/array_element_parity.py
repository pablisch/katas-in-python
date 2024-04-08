from collections import Counter

# This first attempt is on the wrong lines as I misunderstood the question
def solve_1(data):
    data_count = Counter(abs(x) for x in data)
    for item, value in data_count.items():
        if value == 1: 
            return item if item in data else -item

def solve_2(data):
    for x in data: 
        if not -x in data: return x

def solve(data):
    return next(x for x in data if -x not in data)

# codewars solutions

def solve(arr): 
    return sum(set(arr))
# 👆🏻 set() is needed since unopposed numbers may appear multiple times. I did not think of this soltion at all.