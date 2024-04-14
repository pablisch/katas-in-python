def two_to_one(s1, s2):
    return ''.join(sorted(set(s1 + s2)))