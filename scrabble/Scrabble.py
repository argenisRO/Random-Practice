# Scrabble Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed


import random
import string
import sys
import threading
import itertools
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 8
TOTAL_SCORE, TOTAL_ROUNDS, ROBOT_SCORE, ROUND = 0, 0, 0, 0
NUM_OF_ROUND = 2
WORD_FILE = "words.txt"
LINE_SEPERATE = "\n_____________________________________________________"
LOADED = False
DIFFICULTY = 'e'
DIF_CHOICE = {'e': 'Easy', 'm': 'Medium', 'h': 'Hard'}

# TODO:Add score to each round of the game

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}


def loadWords():
    '''
    Loads the words from the file into 'wordsLoaded'
    A Dictionary seperating each letter of the english alphabet
    '''
    allWords = {}

    inFile = open(WORD_FILE, 'r')
    wordList = []
    for e in inFile:
        wordList.append(e.strip().lower())
    inFile.close()

    for word in wordList:
        if word[0] not in allWords:
            allWords[word[0]] = []
        else:
            allWords[word[0]].append(word)
    return allWords


def listWord(wordsLoaded):
    '''
    Loads the words from 'wordsLoaded'
    into a list.
    '''
    tempList = []
    for i in wordsLoaded.values():
        tempList += i
    return tempList


def getWordScore(word, n):
    '''
    Returns the score of a given word
    Also adds 50 if the word matches the 'n' length
    '''
    value = 0
    for letters in word:
        value += SCRABBLE_LETTER_VALUES[letters]
    result = value * len(word)
    if len(word) == n:
        result += 50
    return result


def displayHand(hand):
    '''
    Displays the current hand to the console
    '''
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")
    print()


def returnHand(hand):
    '''
    Returns the current hand to in a list
    '''
    handList = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            handList.append(letter)
    return handList


def dealHand(n):
    '''
    Returns a randomly generated hand given a 'n' length
    '''
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def updateHand(hand, word):
    '''
    Returns a copy of the current hand updated
    With the values altered based on the 'word' given.
    '''
    tempHand = hand.copy()
    for e in word:
        if e in tempHand:
            stored = tempHand.get(e)
            tempHand[e] = stored - 1
    return tempHand


def isValidWord(word, hand, wordsLoaded):
    '''
    Returns True or False based on if 'word'
    Is valid from within 'wordsLoaded' and is not empty.
    '''

    tempHand = hand.copy()

    if word not in listWords:
        return False

    for letter in word:
        if letter not in hand:
            return False
        else:
            stored = tempHand.get(letter)
            tempHand[letter] = stored - 1
            if tempHand[letter] < 0:
                return False
    return True


def calculateHandlen(hand):
    '''
    Returns the sum length of a hand by scanning through 'hand'
    And reading all the Values of each Keys.
    '''
    counter = 0
    for e in hand:
        stored = hand.get(e)
        counter += stored
    return counter


def playHand(hand, wordsLoaded, n):
    '''
    Interactive User Player Base
    '''
    global TOTAL_SCORE
    global ROUND
    invalid = 1
    while calculateHandlen(hand) > 0:
        print('Round', str(ROUND)+'!')
        print("\nCurrent Hand: ", end=' ')
        displayHand(hand)
        if invalid == 4:
            print('Moving on with the game.')
            userInput == '.'
            break

        userInput = input('Enter a word ([.] to finish): ')

        if userInput == '.':
            break

        elif not isValidWord(userInput, hand, wordsLoaded):
            print('Invalid word, please try again.', LINE_SEPERATE)
            invalid += 1

        else:
            invalid = 0
            copy = TOTAL_SCORE
            TOTAL_SCORE += getWordScore(userInput, n)
            added = TOTAL_SCORE - copy
            print('\r"', userInput, '"', 'earned',
                  getWordScore(userInput, n), 'points', LINE_SEPERATE)
            print(' \033[92m+\033[0m Total Score Increased By: \033[92m{}\033[0m'.format(added))
            print('\033[92m', TOTAL_SCORE, '\033[0m'+'vs'+'\033[91m', ROBOT_SCORE, '\033[0m')
            hand = updateHand(hand, userInput)

    if userInput == '.':
        print('Round Over. Total score:', TOTAL_SCORE, 'points.\n')
    else:
        print('You ran out of letters. Total score:', TOTAL_SCORE, 'points.')


def loading():
    '''
    Tiny animation while the bot searches for words
    '''
    print('\n')
    counter = 0

    for dot in itertools.cycle(['.', '..', '...', '\x1b[2K']):
        if LOADED:
            break
        sys.stdout.write('\r' + dot)
        sys.stdout.flush()
        time.sleep(0.7)


def compChooseWord(hand, wordsLoaded, n):
    '''
    Returns the best chosen word from 'wordsLoaded'
    for the computer player
    '''

    bestScore = 0
    bestWord = None

    for handLetter in returnHand(hand):
        stored = wordsLoaded.get(handLetter)
        for word in stored:
            if (DIF_CHOICE[DIFFICULTY] == 'Easy') and (isValidWord(word, hand, wordsLoaded)) and (len(word) <= 2) or \
               (DIF_CHOICE[DIFFICULTY] == 'Medium') and (isValidWord(word, hand, wordsLoaded)) and (len(word) <= 4) or \
               (DIF_CHOICE[DIFFICULTY] == 'Hard') and (isValidWord(word, hand, wordsLoaded)):
                score = getWordScore(word, n)
                if (score > bestScore):
                    bestScore = score
                    bestWord = word
    return bestWord


def compPlayHand(hand, wordsLoaded, n, dif):
    '''
    Computer plays Scrabble against alone.
    '''
    global ROBOT_SCORE
    global LOADED

    totalScore = 0
    while (calculateHandlen(hand) > 0):
        LOADED = False

        print("\nCurrent Hand: ", end=' ')
        displayHand(hand)

        load = threading.Thread(target=loading)
        load.start()
        word = compChooseWord(hand, wordsLoaded, n)
        LOADED = True

        if word == None:
            break

        else:
            if not isValidWord(word, hand, wordsLoaded):
                print("This... can't be happening!")
                break
            else:
                score = getWordScore(word, n)
                ROBOT_SCORE += score
                print('\r"' + word + '" earned ' + str(score) +
                      ' points. Total: ' + str(ROBOT_SCORE) + ' points', LINE_SEPERATE)
                hand = updateHand(hand, word)
                print('\033[92m', TOTAL_SCORE, '\033[0m'+'vs'+'\033[91m', ROBOT_SCORE, '\033[0m')
                print()
    print('\rTotal score: ' + str(ROBOT_SCORE) + ' points.\n')


def choseDifficulty():
    '''
    Greeting message for user asking for 'difficulty' level
    '''
    global DIFFICULTY
    print('\tScrabble', LINE_SEPERATE, '\nChoose A Difficulty',
          '\n• Easy     [e]',
          '\n• Medium   [m]',
          '\n• Hard     [h]')

    while True:
        diffi = input()
        if diffi.lower() not in ['e', 'm', 'h']:
            print("Invalid Input. Please choose between (e), (m), and (h)")
        else:
            print(LINE_SEPERATE)
            DIFFICULTY = diffi
            break


def changeHandSize():
    '''
    Allows the user to change the global HAND_SIZE variable
    '''
    global HAND_SIZE
    print(LINE_SEPERATE, '\nChange Hand Size', '\nCurrent:', HAND_SIZE)
    while True:
        handsize = input('Enter a number or (Cancel [c] )')

        if handsize.lower() in ['cancel', 'c']:
            break

        elif handsize.isdigit():
            HAND_SIZE = int(handsize)
            print('Successfully Changed Your Hand Size', LINE_SEPERATE)
            break
        else:
            print('Only numbers allowed.')


def changeRounds():
    '''
    Allows the user to change the global NUM_OF_ROUND variable
    '''
    global NUM_OF_ROUND
    print(LINE_SEPERATE, '\nChange Rounds', '\nCurrent:', NUM_OF_ROUND)
    while True:
        round = input('Enter a number or (Cancel [c] )')

        if round.lower() in ['cancel', 'c']:
            break

        elif round.isdigit():
            if int(round) >= 1:
                NUM_OF_ROUND = int(round)
                print('Successfully Changed Game Rounds', LINE_SEPERATE)
                break
            else:
                print('Number must be greater than 0.')
        else:
            print('Only numbers allowed.')


def changeDifficulty():
    '''
    Allows the user to change the global DIFFICULTY variable
    '''
    global DIFFICULTY

    print(LINE_SEPERATE, '\nChange Difficulty')
    while True:
        diff = input('Enter a number or (Cancel [c] )')

        if diff.lower() not in DIF_CHOICE:
            print("Invalid Input. Please choose between (e), (m), and (h)")

        else:
            DIFFICULTY = diff
            print('\nSuccessfully Changed Game Difficulty to', DIF_CHOICE[diff])
            break


def endGame(hands):
    '''
    Dismisses the player provinding recorded stats.
    '''
    print(LINE_SEPERATE,
          '\nThanks for playing!',
          '\nDifficulty:', DIF_CHOICE.get(DIFFICULTY),
          '\nTotal Score:\033[92m', TOTAL_SCORE, '\033[0mvs\033[91m', ROBOT_SCORE, '\033[0m',
          '\nTotal Rounds Played:', TOTAL_ROUNDS)


def playGame(wordsLoaded, choice):
    '''
    Scrabble Game
    '''
    global TOTAL_SCORE
    global TOTAL_ROUNDS
    global ROBOT_SCORE
    global HAND_SIZE
    global ROUND
    global NUM_OF_ROUND
    hands, robotHands = 0, 0

    print('\nWelcome to the Scrabble Game!', '\nHand Size:',
          HAND_SIZE)
    while True:
        print(LINE_SEPERATE)
        print('Current Score:', TOTAL_SCORE)
        print('\n• Start Game      [s]',
              '\n• Options         [o]',
              '\n• End Game        [e]')
        userInput = input()
        if userInput.lower() == 's':
            ROUND = 0
            while ROUND < NUM_OF_ROUND:
                ROUND += 1
                TOTAL_ROUNDS += 1

                # Player Turn
                dealtH = dealHand(HAND_SIZE)
                playHand(dealtH, wordsLoaded, HAND_SIZE)
                hands += 1
                # Robot Turn
                dealtI = dealHand(HAND_SIZE)
                compPlayHand(dealtI, wordsLoaded, HAND_SIZE, choice)
                robotHands += 1

            # End of Game
            if TOTAL_SCORE > ROBOT_SCORE:
                print("\033[92mYOU WIN!\033[0m")
                print('\033[92m', TOTAL_SCORE, '\033[0m'+'vs'+'\033[91m', ROBOT_SCORE, '\033[0m')
            else:
                print("\033[91mYOU LOSE!\033[0m")
                print('\033[91m' + str(ROBOT_SCORE), '\033[0m' +
                      'vs'+'\033[92m', str(TOTAL_SCORE), '\033[0m')

        elif userInput.lower() == 'o':
            while True:
                print('\n• Change Hand Size  [h]',
                      '\n• Change Rounds     [r]',
                      '\n• Change Difficulty [d]',
                      '\n• Go Back           [e]')
                optionsInput = input()
                if optionsInput == 'h':
                    changeHandSize()
                elif optionsInput == 'r':
                    changeRounds()
                elif optionsInput == 'd':
                    changeDifficulty()

                elif optionsInput == 'e':
                    break

        elif userInput.lower() == 'e':
            endGame(hands)
            break

        else:
            print('Invalid command.')
    else:  # Safe Check
        print("Something Went Wrong.", "'current' option is set to", choice)


# Start Game
if __name__ == '__main__':
    wordsLoaded = loadWords()
    choseDifficulty()
    listWords = listWord(wordsLoaded)
    playGame(wordsLoaded, DIFFICULTY)
