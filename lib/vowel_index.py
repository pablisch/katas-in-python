def vowel_indices(word):
    vowel_positions = []
    for i in range(1, len(word) + 1):
        if word[i - 1].lower() in ["a", "e", "i", "o", 'u', 'y']:
            vowel_positions.append(i)
    return vowel_positions

vowel_indices("word")

if "a" in ["a", "b", "c"]:
    print ("a is in the array")
else:
    print ("a is NOT in the array")

if "ant" in ["ant", "bee", "cat"]:
    print ("ant is in the array")
else:
    print ("ant is NOT in the array")

if "ant" in "anteater":
    print ("ant is in the word")
else:
    print ("ant is NOT in the word")

# Use enumerator. Still a little obscure to me. Creates an enumerator object as can be seen https://www.w3schools.com/python/ref_func_enumerate.asp
def vowel_positions(word):
    enObj = enumerate(word.lower())
    vowels = "aeiouy"
    return [index + 1 for index, letter in enObj if letter in vowels]

def vowel_positions_concise(word):
    return [index + 1 for index, letter in enumerate(word.lower()) if letter in "aeiouy"]

def vowel_positions_very_concise(word):
    return [i + 1 for i, l in enumerate(word.lower()) if l in "aeiouy"]

vowel_positions("hello")