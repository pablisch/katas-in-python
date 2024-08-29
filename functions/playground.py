word = "hello"
print (word[-1])
print(word[:-1])

def removeExclamtion(str_):
    while str_[-1] == "!": str_ = str_[:-1]
    return str_

# should have used rstrip("!") but I did not realise at the time that it could be used to strip out chars.

removeExclamtion("hjgjhg!!!")
removeExclamtion("hjgjh!g!")
removeExclamtion("hjgjh!g")
removeExclamtion("hjgjh!g!!!!!!!h")
removeExclamtion("hjgjh!g!!!!!!!h!!!")

print (word.rstrip("ol "))