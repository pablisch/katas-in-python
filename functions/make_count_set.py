def make_set_of_count_occurences(iterable):
    item_count_set = set(iterable.count(item) for item in iterable)
    print(item_count_set)

make_set_of_count_occurences('hello')