# https://www.codewars.com/kata/58daa7617332e59593000006/python
# KEYWORDS: sort, max, lambda
# re. max - https://www.programiz.com/python-programming/methods/built-in/max

def most_digits(lst):
    result = lst[0]
    for num in lst:
        if len(str(abs(num))) > len(str(abs(result))): result = num
    return result

# uses max() in a new way to me. Takes 2 args: list and key (which is a function applied to each value)
# so below returns thw arr value with the longest length, i.e. most digits. The abs stops the negative sign from influencing the result.
def most_digits_cw(arr):
    return max(arr, key=lambda x: len(str(abs(x))))

most_digits([9000, 8, 800])