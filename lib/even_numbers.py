def get_last_n_even_numbers_1(data, n):
    return list(filter(lambda x: not x % 2, data))[-n:]

# The problem with this is that it processes the whole list when it may only be necessary to process the last n elements.
# The solution below will process the minimum number of elements

def get_last_n_even_numbers(data, n):
    last_even_els = []
    for x in reversed(data): 
        if x % 2 == 0: last_even_els.append(x)
        if len(last_even_els) >= n: break

    return list(reversed(last_even_els))
