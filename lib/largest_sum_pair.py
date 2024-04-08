def largest_sum_pair(list):
    highest_num = max(list)
    list.remove(highest_num)
    return highest_num + max(list)

# Better ways post submission
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:]) # sort numbers and add the last two, i.e. the highest
