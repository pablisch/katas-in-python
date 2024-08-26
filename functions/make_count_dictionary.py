def make_dict_of_count_occurrences(iterable):
    count_dict = {}  # Create an empty dictionary to store the count of occurrences

    # Iterate through each item in the input iterable
    for item in iterable:
        # Use the .get() method of dictionaries to retrieve the current count of the item.
        # If the item is not yet present in the dictionary, .get() returns 0 by default.
        # Increment the count by 1 and update the dictionary.
        count_dict[item] = count_dict.get(item, 0) + 1

    # After iterating through all items, return the dictionary containing the count of occurrences.
    return count_dict

# using COUNTER package
from collections import Counter

def make_dict_of_count_occurrences_using_Counter(iterable):
    counter_count_dict = Counter(iterable)
    return counter_count_dict 

count2 = make_dict_of_count_occurrences_using_Counter('hello')
print(count2) # => Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Example usage:
iterable = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
# print(make_dict_of_count_occurrences(iterable))

iterable2 = 'hello'
count_dict = make_dict_of_count_occurrences(iterable2)
print(count_dict)
print(count_dict['h'])

my_dict = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
for key, value in my_dict.items():
    print(key, value)

my_dict_view = my_dict.items()
print(my_dict_view)
# => dict_items([('h', 2), ('e', 3), ('l', 2), ('o', 1)])

for key, value in my_dict_view:
    print(key, value)
# => h 2
# => e 3
# => l 2
# => o 1

sorted_dict = dict(sorted(my_dict.items())) # => {'e': 3, 'h': 2, 'l': 2, 'o': 1}
print(sorted_dict)

sorted_dict2 = sorted(my_dict.items())
print(sorted_dict2)

person = dict(name = "John", age = 36, country = "Norway") # => {'name': 'John', 'age': 36, 'country': 'Norway'}
print(person)

x = my_dict.get('h') # => 2
print(x)



my_dict = {'h': 2, 'e': 3, 'l': 2, 'o': 1}
my_dict_view = my_dict.items()

letter = 'h'
if letter in my_dict:
  print(f"The key '{letter}' exists in my_dict")
else:
  print(f"The key '{letter}' does not exist in my_dict")

print(my_dict_view)

my_dict['h'] = 10

print(my_dict_view)

my_dict.update({'h': 7})

print(my_dict_view)

my_dict.update({'h': 7, 'j': 3})

print(my_dict)

print(min(my_dict.values()))
print(max(my_dict.values()))

# my_dict = {'e': 3, 'h': 2, 'l': 2, 'o': 1}

# Find the minimum value
min_value = min(my_dict.values())

# Find the maximum value
max_value = max(my_dict.values())

# print("Minimum value:", min_value)
# print("Maximum value:", max_value)