# Hangman game
# ArgenisRO
#
# Test Commit
# 6.00.1x hangman example with my own little twist.


import random
import string as s

WORDFILE = "./files/words.txt"


def loadWords():
    '''
    Loads the words from the file into (wordsLoaded)
    '''
    inFile = open(WORDFILE, 'r')
    line = inFile.readline()
    wordsLoaded = line.split()
    print(len(wordsLoaded), "words loaded.")
    return wordsLoaded


def chooseWord(wordsLoaded):
    '''
    Chooses a random word from the file provided.
    '''
    return random.choice(wordsLoaded)


def isWordGuessed(hiddenWord, lettersGuessed):
    '''
    Checks if the full word has been guessed yet.
    '''
    for letter in hiddenWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(hiddenWord, lettersGuessed):
    '''
    Returns the guessed words so far. Adds a underscore for unguessed letters.
    '''
    guesedCorrect = ''
    for letter in hiddenWord:
        if letter in lettersGuessed:
            guesedCorrect += letter
        else:
            guesedCorrect += '_ '
    return guesedCorrect


def getAvailableLetters(lettersGuessed):
    '''
    Returns the available letters based on user inputs
    '''
    alphabet = list(s.ascii_lowercase)  # retrieve in a list the alphabet from string library.
    for e in lettersGuessed:
        if e in alphabet:
            alphabet.remove(e)
    return ''.join(alphabet)


def getUserInputGuess():
    '''
    Returns the user for input making sure it's a proper whole number.
    '''
    while True:  # constantly check until the user provides a proper whole number.
        try:
            userGuesses = int(input("How many guesses would you like to have? "))
            break
        except:
            print("Please enter a valid number.")
            print("-------------")
    return userGuesses


def getUserInputLetter():
    '''
    Makes sure the user is inputing only ONE character from the alphabet.
    '''
    while True:
        userInput = input("Please guess a letter: ")
        if userInput.isalpha():
            if len(userInput) == 1:
                return userInput
        print("Please enter only ONE letter from a - z")
        print("-------------")


# made these into their own functions incase I'd like to use them later
def alreadyGuessed(hiddenWord, lettersGuessed):
    return "You already guessed that letter: " + getGuessedWord(hiddenWord, lettersGuessed)


def notGuessed(hiddenWord, lettersGuessed):
    return "That letter is NOT in my word: " + getGuessedWord(hiddenWord, lettersGuessed)


def goodGuessed(hiddenWord, lettersGuessed):
    return "Good guess:" + getGuessedWord(hiddenWord, lettersGuessed)
# ___________


def hangman(hiddenWord):
    '''
    Hangman Game
    '''
    print("-------------")
    print("Welcome to the Hangman Game!")
    print("-------------")
    userGuesses = getUserInputGuess()
    numofGussesLeft = int(userGuesses)
    lettersGuessed = []
    if numofGussesLeft < 3:  # For brave people only
        print("You are a brave one. Are you feeling confident?")
    print("-------------")
    print("I am thinking of a word that is", len(hiddenWord), "letters long.")
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

        userInput = getUserInputLetter()
        userInput = userInput.lower()

        if userInput in hiddenWord:
            if userInput in lettersGuessed:
                print(alreadyGuessed(hiddenWord, lettersGuessed))

            else:
                # fixed 'good guess' showing up even with the letter already guessed.
                lettersGuessed.append(userInput)
                print(goodGuessed(hiddenWord, lettersGuessed))
        else:
            if userInput in lettersGuessed:
                print(alreadyGuessed(hiddenWord, lettersGuessed))
            else:
                lettersGuessed.append(userInput)
                numofGussesLeft -= 1
                print(notGuessed(hiddenWord, lettersGuessed))


# ___________Run Game___________
wordsLoaded = loadWords()  # Loads the words from the provided TXT file.
hiddenWord = chooseWord(wordsLoaded).lower()  # Selects a word from random and makes it undercase.
hangman(hiddenWord)  # runs the game
