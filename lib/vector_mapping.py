def map_vector1(vector, circle1, circle2):
    x1_vect_off = vector[0] - circle1[0]
    y1_vect_off = vector[1] - circle1[1]
    radius_diff = circle2[2] / circle1[2]

    return (round(x1_vect_off * radius_diff, 2) + circle2[0], round(y1_vect_off * radius_diff, 2) + circle2[1])

def map_vector(v, c1, c2):
    return (round((v[0]-c1[0]) * c2[2]/c1[2], 2) +c2[0], round((v[1]-c1[1]) * c2[2]/c1[2], 2) +c2[1])