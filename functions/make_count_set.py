# counts the number of times that something appears, e.g. the number of times a char appear in a string.
# the set only holds unique values. It does not show what appears x times, only that something did.
def make_set_of_count_occurences(iterable):
    item_count_set = set(iterable.count(item) for item in iterable)
    print(item_count_set)

# this counts how many unique char counts there are in 'hello' => {1, 2} since l appears twice and other letters once.
make_set_of_count_occurences('hello')

# as above => {1, 6} since e appears six times.
make_set_of_count_occurences('heeeeee')