def intersection(strArr):
    str1 = list(map(int, strArr[0].split(', ')))
    str2 = list(map(int, strArr[1].split(', ')))
    nums = list(set(str1) & set(str2))
    strings = map(str, nums)
    return ','.join(strings)

# intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"])