def sum_of_nth_term_1(n):
    # create a range from 1 to n inclusive
    # apply function to each num in range
    # sum the results of each

    nums = list(range(1, n + 1))
    terms = map(lambda y: 1 / (((y - 1) * 3) + 1), nums)
    terms_list = list(terms)

    return round(sum(terms_list), 2)

def sum_of_nth_term_2(n):
    nums = range(1, n + 1)
    terms = map(lambda y: 1 / (((y - 1) * 3) + 1), nums)

    return round(sum(terms), 2)

def sum_of_nth_term_3(n):
    terms = map(lambda y: 1 / (((y - 1) * 3) + 1), range(1, n + 1))
    return round(sum(terms), 2)

def sum_of_nth_term_4(n):
    return '{0:.2f}'.format(round(sum(map(lambda y: 1 / (((y - 1) * 3) + 1), range(1, n + 1))), 2))

def sum_of_nth_term(n):
    return '{0:.2f}'.format(sum(map(lambda y: 1 / (y * 3 + 1), range(n))))

# codewars better solutions

def series_sum_1(n):
    return '{:.2f}'.format(sum(1 / (3 * i + 1) for i in range(n)))

def series_sum(n):
    sum = 0
    for i in range(n):
        sum += 1 / (1 + 3 * i)
    return '%.2f' % sum