import math

def process_data_1(data):
    return math.prod([x[0] - x[1] for x in data])

def process_data_2(data):
    diffs = [x[0] - x[1] for x in data] # a - b in each nested list
    return math.prod(diffs) # find the product of all items in the list

def process_data(data):
    return math.prod(map(lambda x: x[0] - x[1], data))