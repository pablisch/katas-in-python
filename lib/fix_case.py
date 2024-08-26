import re

def solve_with_regex(str_):
    return str_.upper() if len(re.findall(r'[A-Z]', str_)) > len(re.findall(r'[a-z]', str_)) else str_.lower()

def solve_with_regex_revision(str_):
    return str_.upper() if len(re.findall(r'[A-Z]', str_)) * 2 > len(str_) else str_.lower()

# NOTE the complaint about type. str.isupper return true or false but this also equates to 1 or 0.
def solve_concise(s):
    return s.upper() if sum(map(str.isupper, s)) > sum(map(str.islower, s)) else s.lower()

# NOTE the complaint about type. str.isupper return true or false but this also equates to 1 or 0.
def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()
