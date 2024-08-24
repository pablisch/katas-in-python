def add_length(str):
    words = str.split()
    return list(map(lambda word: f'{word} {len(word)}', words))