# Hangman game
#
# Test Commit


import random
import string as s

WORDLIST_FILE = "words.txt"


def loadWords():
    inFile = open(WORDLIST_FILE, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(len(wordlist), "words found.")
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)


wordlist = loadWords()


def isWordGuessed(hiddenWord, lettersGuessed):
    for letter in hiddenWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(hiddenWord, lettersGuessed):
    guesedCorrect = ''
    for letter in hiddenWord:
        if letter in lettersGuessed:
            guesedCorrect += letter
        else:
            guesedCorrect += '_ '
    return guesedCorrect


def getAvailableLetters(lettersGuessed):
    alphabet = list(s.ascii_lowercase)
    for e in lettersGuessed:
        if e in alphabet:
            alphabet.remove(e)
    return ''.join(alphabet)


def hangman(hiddenWord):
    '''
    Hangman Game
    '''
    print("-------------")
    print("Welcome to the Hangman Game!")
    print("-------------")
    userGuesses = input("How many guesses would you like to have? ")
    print("-------------")
    print("I am thinking of a word that is", len(hiddenWord), "letters long.")
    numofGussesLeft = int(userGuesses)
    lettersGuessed = []
    while True:
        print("-------------")

        if numofGussesLeft == 0:
            print("You Lost!")
            print("The word was", hiddenWord)
            break
        if isWordGuessed(hiddenWord, lettersGuessed):
            print("You won!")
            break

        print(" -- You have", numofGussesLeft, "guesses left -- ")
        print("Available Letters:", getAvailableLetters(lettersGuessed))

        userInput = input("Please guess a letter: ")
        userInput = userInput.lower()

        if userInput in hiddenWord:
            if userInput in lettersGuessed:
                print("You already guessed that letter: ",
                      getGuessedWord(hiddenWord, lettersGuessed))

            lettersGuessed.append(userInput)
            print("Good guess:", getGuessedWord(hiddenWord, lettersGuessed))
        else:
            if userInput in lettersGuessed:
                print("You already guessed that letter: ",
                      getGuessedWord(hiddenWord, lettersGuessed))
            else:
                lettersGuessed.append(userInput)
                numofGussesLeft -= 1
                print("That letter is NOT in my word: ",
                      getGuessedWord(hiddenWord, lettersGuessed))


hiddenWord = chooseWord(wordlist).lower()
hangman(hiddenWord)
