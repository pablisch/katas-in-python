def sort_and_star(list):
    return '***'.join(sorted(list)[0])

def sort_and_star_mk1(list):   
    list.sort()
    return '***'.join(list[0])    

def sort_and_star_mk3(list):
    return '***'.join(min(list))

my_list = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]

print(sort_and_star_mk3(my_list))