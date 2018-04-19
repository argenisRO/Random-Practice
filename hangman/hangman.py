# Hangman Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed


import random
import string as s

WORD_FILE = "words.txt"
LINE_SEPERATE = "\n______________"


def loadWords():
    '''
    Loads the words from the file into (wordsLoaded)
    '''
    inFile = open(WORD_FILE, 'r')
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
            guesedCorrect += ' ' + letter + ' '
        else:
            guesedCorrect += ' _ '
    return guesedCorrect + LINE_SEPERATE


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
    while True:  # constantly check until the user provides a proper positive number.
        try:
            userGuesses = int(input("How many guesses would you like to have? "))
            if userGuesses > 0:
                break
            else:
                print("Please enter a valid positive number." + LINE_SEPERATE)
        except(ValueError):
            print("Please enter a valid positive number." + LINE_SEPERATE)
            continue

    return userGuesses


def getUserInputLetter():
    '''
    Makes sure the user is inputing only ONE character from the alphabet.
    '''
    while True:
        userInput = input("Guess a letter: ")
        if userInput.isalpha():
            if len(userInput) == 1:
                return userInput
        print("Please enter only ONE letter from a - z" + LINE_SEPERATE)


def alreadyGuessed(hiddenWord, lettersGuessed):
    return '{}                    {}'.format("\033[93mAlready Guessed:\033[0m", getGuessedWord(hiddenWord, lettersGuessed))


def notGuessed(hiddenWord, lettersGuessed):
    return '{}                              {}'.format("\033[91mWrong:\033[0m", getGuessedWord(hiddenWord, lettersGuessed))


def goodGuessed(hiddenWord, lettersGuessed):
    return '{}                               {}'.format("\033[92mGood:\033[0m", getGuessedWord(hiddenWord, lettersGuessed))


def hangman(hiddenWord):
    '''
    Hangman Game
    '''
    print('\t\tHangman')

    userGuesses = getUserInputGuess()
    numofGussesLeft = int(userGuesses)
    lettersGuessed = []

    if numofGussesLeft < 3:  # For brave people only
        print("You are a brave one. Are you feeling confident?")
    print(LINE_SEPERATE[1:] + "\nI am thinking of a word that is",
          len(hiddenWord), "letters long." + LINE_SEPERATE)
    while True:
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
                lettersGuessed.append(userInput)
                print(goodGuessed(hiddenWord, lettersGuessed))
        else:
            if userInput in lettersGuessed:
                print(alreadyGuessed(hiddenWord, lettersGuessed))
            else:
                lettersGuessed.append(userInput)
                numofGussesLeft -= 1
                print(notGuessed(hiddenWord, lettersGuessed))


# Start Game
if __name__ == '__main__':
    wordsLoaded = loadWords()
    hiddenWord = chooseWord(wordsLoaded).lower()
    hangman(hiddenWord)
