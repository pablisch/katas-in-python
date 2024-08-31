# KEYWORDS: dictionary, get, in_dictionary, includes, reference, match

orders = {
    "jabroni": "Patron Tequila",
    "school counselor":	"Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member":	"Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
}

def bartender(input):
    if input.lower() in orders: return orders[input.lower()]
    return "beer"

bartender("JAbronis")
bartender("JAbroni")

# There are plenty of more concise ways of writing this and the key is to use .get()
# I was not sure that .get() would not return an error if not match was found.

d = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
}

def get_drink_by_profession(s):
    return d.get(s.lower(), "Beer")
# 👆🏼returns "Beer" if no match found.

# 👇🏻similar to above but calls the dictionary directly
def get_drunk_by_profession(param):
    return {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }.get(param.title(), "Beer")