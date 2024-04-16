import re

def validate(strParam):
    correct_chars = bool(re.search("^[a-zA-Z\\d_]{4,25}$", strParam))
    letter_start = bool(re.search("[a-zA-Z]", strParam[0]))
    let_num_end = bool(re.search("[^_]", strParam[-1]))

    return str(correct_chars and letter_start and let_num_end)


# print(validate('a2aaaa_A'))