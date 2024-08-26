import re

# I naturally went to regex but this seems like an unpopular choice and Python has plenty of great ways to deal with this without regex.
def same_case(a, b):
    if not re.match('[a-zA-Z]', a) or not re.match('[a-zA-Z]', b): return -1
    if bool(re.match('[a-z]', a)) == bool(re.match('[a-z]', b)):
        return 1
    else: return 0

# A simple approach although some will be critical of nested conditionals
def same_case_simple(a, b):
    if a.isalpha() and b.isalpha():
        if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
            return 1
        else:
            return 0
    else:
        return -1

# concise and smart but less readable. The middle part, if a.isalpha() and b.isalpha(), is the condition,
# a.isupper() == b.isupper() returns true or 1 when they match and 0 if they do not. I always forget this.
def same_case_concise(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1

# simple combining of the two chars
def same_case_combined(a, b):
    c = a+b
    if not c.isalpha():
        return -1
    if c.islower() or c.isupper():
        return 1
    else:
        return 0