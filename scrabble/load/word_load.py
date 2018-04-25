# Scrabble Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed


allWords = {}
wordList = []

with open("load/words.txt", 'r') as wordFile:
    for e in wordFile:
        wordList.append(e.strip().lower())

for word in wordList:
    if word[0] not in allWords:
        allWords[word[0]] = []
    else:
        allWords[word[0]].append(word)
