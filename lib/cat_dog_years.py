def owned_cat_and_dog(cat_years, dog_years):
    cat_owned = 0 if cat_years < 15 else 1 if cat_years < 24 else 2 + ((cat_years - 24) // 4)
    dog_owned = 0 if dog_years < 15 else 1 if dog_years < 24 else 2 + ((dog_years - 24) // 5)
    return [cat_owned, dog_owned]

# Nice codewars solution
def owned_cat_and_dog(cat_years, dog_years):
    h1 = (cat_years > 14 ) + (cat_years > 23) + max(0, (cat_years - 24) // 4)
    h2 = (dog_years > 14 ) + (dog_years > 23) + max(0, (dog_years - 24) // 5)
    return [h1, h2]