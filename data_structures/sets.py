set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # Output: {4, 5}

# Difference
difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1, 2, 3}

# Symmetric Difference
symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

print(5 in set1) # => True
print(6 in set1) # => False

for item in set1:
    print(item) # => 1\n 2\n 3\n 4\n 5\n 

set1.add(6) # => set1 == {1, 2, 3, 4, 5, 6}

# add any iterable to a set - mutates and returns None
set1.update(set2)
print(set1) # => {1, 2, 3, 4, 5, 6, 7, 8}

set1.update([2, 10, 13])
print(set1) # => {1, 2, 3, 4, 5, 6, 7, 8, 10, 13}

# remove an item - mutates, returns None and throw error is item does not exist
set1.remove(1)
print(set1) # => {2, 3, 4, 5, 6, 7, 8, 10, 13}
# set1.remove(100) # => KeyError: 100

# remove an item - mutates, returns None and does NOT throw an error if the item does not exist
set1.discard(2)
print(set1) # => {3, 4, 5, 6, 7, 8, 10, 13}

# clear the set - mutates and returns None
set1.clear()
print(set1) # => set()

# delete a set
del set1
# print(set1) # => NameError: name 'set1' is not defined. Did you mean: 'set2'?



