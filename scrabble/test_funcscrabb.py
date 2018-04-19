# Scrabble Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed

from scrabble import *

# Unit Test


def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def test_getWordScore():
    """
    Unit test for getWordScore
    """
    FAILED = False
    words = {("", 7): 0, ("it", 7): 4, ("was", 7): 18, ("scored", 7): 54,
             ("waybill", 7): 155, ("outgnaw", 7): 127, ("fork", 7): 44, ("fork", 4): 94}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print("FAILED: test_getWordScore()")
            print("\tExpected", words[(word, n)], "points but got '" +
                  str(score) + "' for word '" + word + "', n=" + str(n))
            FAILED = True
    if not FAILED:
        print("SUCCESSFUL: test_getWordScore()")


def test_updateHand():
    """
    Unit test for updateHand
    """
#__Test__ 1
    handOrig = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l': 1, 'm': 1}
    expectedHand2 = {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILED: test_updateHand('" + word + "', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return
    if handCopy != handOrig:
        print("FAILED: test_updateHand('" + word + "', " + str(handOrig) + ")")
        print("\tOriginal Hand:", handOrig)
        print("\tNew Hand:", handCopy)

        return

# __Test 2__
    handOrig = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v': 1, 'n': 1, 'l': 1}
    expectedHand2 = {'e': 0, 'v': 1, 'n': 1, 'i': 0, 'l': 1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILED: test_updateHand('" + word + "', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- expected:", expectedHand1, "or", expectedHand2)

        return

    if handCopy != handOrig:
        print("FAILED: test_updateHand('" + word + "', " + str(handOrig) + ")")
        print("\tOriginal Hand:", handOrig)
        print("\tNew Hand:", handCopy)

        return

#__Test__ 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILED: test_updateHand('" + word + "', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- expected:", expectedHand1, "or", expectedHand2)

        return

    if handCopy != handOrig:
        print("FAILED: test_updateHand('" + word + "', " + str(handOrig) + ")")
        print("\tOriginal Hand:", handOrig)
        print("\tNew Hand:", handCopy)

        return

    print("SUCCESSFUL: test_updateHand()")


def test_isValidWord(wordsLoaded):
    """
    Unit test for isValidWord
    """
    FAILED = False
#__Test__ 1
    word = "hello"
    handOrig = getFrequencyDict(word)
    handCopy = handOrig.copy()

    if not isValidWord(word, handCopy, wordsLoaded):
        print("FAILED: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        FAILED = True

#__Test to see if wordsLoaded or hand have been modified__
    if not isValidWord(word, handCopy, wordsLoaded):
        print("FAILED: test_isValidWord()")

        if handCopy != handOrig:
            print('\t', word, "Tested a second time.")
            print("\tHand should be", handOrig, "but instead it is", handCopy)

        else:
            wordInWL = word in wordsLoaded
            print("The word", word, "should be in wordsLoaded.", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        FAILED = True

#__Test__ 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
    word = "rapture"

    if isValidWord(word, hand, wordsLoaded):
        print("FAILED: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        FAILED = True

#__Test__ 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
    word = "honey"

    if not isValidWord(word, hand, wordsLoaded):
        print("FAILED: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        FAILED = True

#__Test__ 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}
    word = "honey"

    if isValidWord(word, hand, wordsLoaded):
        print("FAILED: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        FAILED = True

#__Test__ 5
    hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    word = "evil"

    if not isValidWord(word, hand, wordsLoaded):
        print("FAILED: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        FAILED = True

#__Test__ 6
    word = "even"

    if isValidWord(word, hand, wordsLoaded):
        print("FAILED: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        FAILED = True

    if not FAILED:
        print("SUCCESSFUL: test_isValidWord()")


wordsLoaded = loadWords()
print("_______________________________")
print("Testing getWordScore...")
test_getWordScore()
print("_______________________________")
print("Testing updateHand...")
test_updateHand()
print("_______________________________")
print("Testing isValidWord...")
test_isValidWord(wordsLoaded)
print("_______________________________")
