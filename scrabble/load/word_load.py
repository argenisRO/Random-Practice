# Scrabble Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed


allWords = {}
wordList = []

with open("load/words.txt", 'r') as wordFile:
    for line in wordFile:
        word = line.strip().lower()
        if word[0] not in allWords:
            allWords[word[0]] = []
        else:
            allWords[word[0]].append(word)
