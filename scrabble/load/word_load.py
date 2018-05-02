# Scrabble Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed


allWords = {}

with open("load/words.txt", 'r') as wordFile:
    '''
    Loads all the words into the 'allWords'
    Dictionary with each Key being a letter of the alphabet
    and its Value the words starting with that letter.

    Sorts the Values according to the word's length.
    '''

    for line in wordFile:
        word = line.strip().lower()
        if word[0] not in allWords:
            allWords[word[0]] = []
        else:
            allWords[word[0]].append(word)

    for x in allWords:
        allWords[x].sort(key=len)
