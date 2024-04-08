def get_multiples(integer, limit):
  i = integer
  multiples = []
  while i <= limit:
    multiples.append(i)
    i += integer
  return multiples

def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))

# list() creates a list from an iterable
# in ths case, list() is given a range
# the range starts at integer, goes to one beyond interger (non-inclusive) and has a step interval of integer
