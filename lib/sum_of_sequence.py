# https://www.codewars.com/kata/586f6741c66d18c22800010a/solutions/python

def sequence_sum(begin_number, end_number, step):
    sequence = []
    for i in range (begin_number, end_number + 1, step):
        sequence.append(i)
    return sum(sequence)

def sequence_sum_concise(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))

