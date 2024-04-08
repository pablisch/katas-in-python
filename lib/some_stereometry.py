import math

def stereometry(r, h):
    circ_r = math.sqrt((r-h) * (2*r - (r-h)))
    return (round(4 * math.pi * r ** 2, 3), round(math.pi * circ_r ** 2, 3), round(2 * math.pi * circ_r, 3))
