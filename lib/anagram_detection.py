def anagram_detection(test, original):
    return sorted(test.lower()) == sorted(original.lower())