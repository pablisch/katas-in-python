import math

def circle_area_inside_square_1(area_of_square):
    pi = math.pi
    radius = math.sqrt(area_of_square) / 2
    area_of_circle = radius ** 2 * pi
    return round(area_of_circle, 8)

def circle_area_inside_square(size):
    return round((math.sqrt(size) / 2) ** 2 * math.pi, 8)

def square_area_to_circle(size):
    return size * math.pi / 4
