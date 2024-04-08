from collections import Counter

def trilingual_democracy(group):
    if len(set(group)) == 1: return group[0]
    if len(set(group)) == 3: return list(set('DFIK') - set(group))[0]
    count = Counter(group)
    for key, value in count.items():
        if value == 1: return key

# from codewars soultions

def trilingual_democracy(group: str) -> str:
    
    _set = set(group)
    
    if len(_set) == 1: return group[0]
    if len(_set) == 3: return next(iter(set('DFIK') - _set))

    return min(group, key=group.count)

def trilingual_democracy(group):
    return chr(ord(group[0])^ord(group[1])^ord(group[2]))

from functools import reduce

def trilingual_democracy(group):
    return chr(reduce(int.__xor__, map(ord, group)))

from functools import reduce
from operator import xor

def trilingual_democracy(group):
    return chr(reduce(xor, (ord(c) for c in group)))
