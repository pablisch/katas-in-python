def form_the_minimum(list):
    string_set = set(str(item) for item in list)
    return int(''.join(sorted(string_set)))

def form_the_minimum(list):
    return int(''.join(sorted(set(str(item) for item in list))))

# codewars solutions
def min_value1(digits):
    return int("".join(map(str, sorted(set(digits)))))
# 👆🏻 set(digits) removes any duplicates.
# sorted(set(digits)) => the sorted sorts them into ascending order.
# (str,sorted(set(digits))) => the comma here is new to me. It is explained by understanding the map func in python.
# map(function, iterable) => map takes a function and iterable sepearated by a comma. The result is the function applied to each element of the iterable.
# so, map(str, sorted(set(digits))) applies str() to each of the sorted set of unique digits.
# being strings, they can be joined and then the result is turned into an integer.

def min_value2(digits):
    return int("".join(str(x) for x in sorted(set(digits))))
# 👆🏻 set(digits) removes any duplicates.
# sorted(set(digits)) => the sorted sorts them into ascending order.
# str(x) for x in ... => turns each of the integers in the sorted set into a string so they can be joined.
# being strings, they can be joined and then the result is turned into an integer.