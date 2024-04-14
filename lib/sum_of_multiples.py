def sum_of_multiples(n, m):
    return "INVALID" if n < 0 or m < 0 or n * m == 0 else sum(range(n, m, n))