import math

def cook_pancakes(n, m):
    print(f"cakes = {n}, capacity = {m}, time = {math.ceil((n * 2) / m)} and min = {2}")
    return max(2, math.ceil((n * 2) / m))