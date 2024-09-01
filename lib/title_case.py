# https://www.codewars.com/kata/5202ef17a402dd033c000009/python
# KEYWORDS: title_case, titlecase, conditional, include, replace, capitalise, for, enumerate

# NOTE: there is a problem in the code below since the string lowers could contain a partial match in the check: if words[i] in lowers, e.g. if 'To' was checked against 'And In Toe' it would wrongly make a match.
def title_case_wrong(s1, s2 = ''):
    words = s1.title().split()
    lowers = s2.title()
    for i in range(1, len(words)):
        if words[i] in lowers: words[i] = words[i].lower()
    return ' '.join(words)

def title_case(s1, s2 = ''):
    words = s1.title().split()
    lowers = s2.title().split()
    for i in range(1, len(words)):
        if words[i] in lowers: words[i] = words[i].lower()
    return ' '.join(words)


title_case('THE WIND IN THE WILLOWS', 'The In')
print ('\n')
title_case('THE WIND IN THE WILLOWS')

# CW to look at...

# This is really clever, looking at it. .capitalize() makes only the first char uppercase and all others are lowercase, e.g. 'The wind in the willows'.
# All the minor_words are made lowercase
# The list comprehension iterates over the words in the title array =>
# if the word is in minor_words then it goes in as a lowercase word as it is, otherwise it is capitalised.
# the first word is always capitalised since it started that way and so is never found in minor_words.
def title_case_cw_1(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

# This is pretty much the same as my solution and maybe a little scrappier
def title_case_cw_2(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)

# at first glance, this is horrible code. The usual one-liner nonsense.
# example: for ('THE WIND IN THE WILLOWS', 'The In')
# the first step is title.lower().split() => 'the wind in the willows'
# this is enumerated => [(0, 'the'), (1, 'wind'), (2, 'in'), (3, 'the'), (4, 'willows')]
# 👆🏼this is a good step, to get the index and word!
# then there is an if/else with only two possible outcomes:
# IF the word is in minor_words AND index exists (i.e. i is NOT 0, the first word) THEN just use the word, e.g. (0, 'the') is NOT word because it has the index of 0, (1, 'wind') is NOT word because it is NOT in minor_words but (3, 'the') IS word because it has a positive index AND it is in minor_words.
# ELSE use word capitalised.
# NOTE: the iteration syntax which is unfamiliar to me, 'for i, w in...', just like having forEach((index, word) => ...) in JS.
def title_case_cw_3(title, minor_words=''):
    return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))