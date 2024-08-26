from math import sqrt

def predict_age_basic(age1, age2, age3, age4, age5, age6, age7, age8):
    ages = [age1, age2, age3, age4, age5, age6, age7, age8]
    squares = [age ** 2 for age in ages]
    total_of_squares = sum(squares)
    return int(sqrt(total_of_squares) // 2)

def predict_age(age1, age2, age3, age4, age5, age6, age7, age8):
    return sqrt(sum([age ** 2 for age in [age1, age2, age3, age4, age5, age6, age7, age8]])) // 2

# Apparently square root can be written as x ** 0.5 so there is no need to import sqrt from math.
# Also learned that args can be mashed together as *ages or *args, etc.

def predict_age_concise(*ages):
    return sum([age ** 2 for age in ages]) ** 0.5 // 2

predict_age(65, 60, 75, 55, 60, 63, 64, 45)

root = sqrt(9)

print (9 ** 0.5 == 3)