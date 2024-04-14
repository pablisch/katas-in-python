import re

def validate_username(username):
    return bool(re.search("^[a-z\\d_]{4,16}$", username))