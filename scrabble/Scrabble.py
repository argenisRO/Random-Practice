# Scrabble Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed


import random
import string
import sys
import threading
import itertools
import time
import load.word_load
import load.ascii

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 8
TOTAL_SCORE, TOTAL_ROUNDS, ROBOT_SCORE, ROUND = 0, 0, 0, 0
NUM_OF_ROUND = 2
LINE_SEPERATE = "\n" * 100
LOADED = False
wordsLoaded = load.word_load.allWords
listWords = load.word_load.wordList
DIFFICULTY = 'e'
DIF_CHOICE = {'e': '\033[92mEasy\033[0m', 'm': '\033[93mMedium\033[0m', 'h': '\033[91mHard\033[0m'}


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}


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
        print('Round', str(ROUND) + '!')
        print('\n'*10)
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
            print('Invalid word, please try again.')
            invalid += 1

        else:
            invalid = 0
            copy = TOTAL_SCORE
            TOTAL_SCORE += getWordScore(userInput, n)
            added = TOTAL_SCORE - copy
            print('\r"', userInput, '"', 'earned',
                  getWordScore(userInput, n), 'points')
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
                      ' points. Total: ' + str(ROBOT_SCORE) + ' points')
                hand = updateHand(hand, word)
                print('\033[92m', TOTAL_SCORE, '\033[0m'+'vs'+'\033[91m', ROBOT_SCORE, '\033[0m')
                print()
    print('\rTotal score: ' + str(ROBOT_SCORE) + ' points.\n')


def introduction():
    '''
    User greeting message asking for the 'difficulty' level
    '''
    global DIFFICULTY
    centered = '\t'*9
    print(LINE_SEPERATE)

    while True:
        load.ascii.titleArt()
        load.ascii.difficultyArt()
        print(centered, '    Easy     [e]')
        print(centered, '    Medium   [m]')
        print(centered, '    Hard     [h]')
        diffi = input(centered+'           ')
        if diffi.lower() not in ['e', 'm', 'h', 'easy', 'medium', 'hard']:
            print(LINE_SEPERATE)
            print(centered, "     Invalid Input.")
            print(('\t'*8), "Please choose between (e), (m), and (h)")
        else:
            print(LINE_SEPERATE)
            DIFFICULTY = diffi
            break


def changeHandSize():
    '''
    Allows the user to change the global HAND_SIZE variable
    '''
    global HAND_SIZE
    centered = '\t'*9
    print(LINE_SEPERATE)

    while True:
        load.ascii.titleArt()
        load.ascii.optionsArt()
        print(centered + "     \033[1mCHANGE HAND SIZE\033[0m\n")
        print(centered, "Current Hand Size: {}".format(HAND_SIZE))
        print(centered, "Enter a number\n", centered, '[b] to go back')

        handsize = input(centered+'             ')

        if handsize.lower() in ['back', 'b']:
            print(LINE_SEPERATE)
            break

        elif handsize.isdigit():
            if int(round) >= 1:
                print(LINE_SEPERATE)
                HAND_SIZE = int(handsize)
                print(centered, 'Successfully Changed Your Hand Size')
                break
            else:
                print(LINE_SEPERATE)
                print(centered, 'Number must be greater than 0.')
        else:
            print(LINE_SEPERATE)
            print(centered, 'Only numbers allowed.')


def changeRounds():
    '''
    Allows the user to change the global NUM_OF_ROUND variable
    '''
    global NUM_OF_ROUND
    centered = '\t'*9
    print(LINE_SEPERATE)

    while True:
        load.ascii.titleArt()
        load.ascii.optionsArt()
        print(centered + "     \033[1mCHANGE ROUNDS\033[0m\n")
        print(centered, "Current Rounds: {}".format(NUM_OF_ROUND))
        print(centered, "Enter a number\n", centered, '[b] to go back')

        round = input(centered+'             ')

        if round.lower() in ['back', 'b']:
            print(LINE_SEPERATE)
            break

        elif round.isdigit():
            if int(round) >= 1:
                print(LINE_SEPERATE)
                NUM_OF_ROUND = int(round)
                print(centered, 'Successfully Changed Game Rounds')
                break
            else:
                print(LINE_SEPERATE)
                print(centered, 'Number must be greater than 0.')
        else:
            print(LINE_SEPERATE)
            print(centered, 'Invalid Input')


def changeDifficulty():
    '''
    Allows the user to change the global DIFFICULTY variable
    '''
    global DIFFICULTY
    centered = '\t'*9
    print(LINE_SEPERATE)

    while True:
        load.ascii.titleArt()
        load.ascii.optionsArt()

        print(centered + "     \033[1mCHANGE DIFFICULTY\033[0m\n")
        print(centered, "Current Difficulty: {}".format(DIF_CHOICE[DIFFICULTY]))
        print(
            centered, "Enter a difficulty:\n", centered, "Easy[e], Medium[m] or Hard[h]\n", centered, '[b] to go back')

        userDifficulty = input(centered+'             ')

        if userDifficulty.lower() in ['back', 'b']:
            print(LINE_SEPERATE)
            break

        if userDifficulty.lower() not in DIF_CHOICE:
            print(LINE_SEPERATE)
            print(('\t'*7), "   Invalid Input. Please choose between (e), (m), and (h)")

        else:
            print(LINE_SEPERATE)
            DIFFICULTY = userDifficulty
            print(('\t'*8), 'Successfully Changed Game Difficulty to',
                  DIF_CHOICE[userDifficulty])
            break


def endGame(hands):
    '''
    Dismisses the player provinding recorded stats.
    '''
    centered = '\t'*9
    print(LINE_SEPERATE)

    load.ascii.titleArt()
    load.ascii.endArt()

    print(centered, 'Difficulty:', DIF_CHOICE[DIFFICULTY])
    print(centered, 'Total Score:\033[92m', TOTAL_SCORE,
          '\033[0mvs\033[91m', ROBOT_SCORE, '\033[0m')
    print(centered, 'Total Rounds Played:', TOTAL_ROUNDS)


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
    centered = '\t'*9

    while True:
        load.ascii.titleArt()
        load.ascii.menuArt()
        print(centered, '• Start Game      [s]')
        print(centered, '• Options         [o]')
        print(centered, '• End Game        [b]')

        userInput = input('\n'+centered+'           ')

        if userInput.lower() == 's':
            ROUND = 0
            while ROUND < NUM_OF_ROUND:
                ROUND += 1
                TOTAL_ROUNDS += 1

                # Player Turn
                dealtH = dealHand(HAND_SIZE)
                playHand(dealtH, wordsLoaded, HAND_SIZE)
                hands += 1
                print(LINE_SEPERATE)
                # Robot Turn
                dealtI = dealHand(HAND_SIZE)
                compPlayHand(dealtI, wordsLoaded, HAND_SIZE, choice)
                robotHands += 1
                print(LINE_SEPERATE)

            # End of Game
            if TOTAL_SCORE > ROBOT_SCORE:
                print("\033[92mYOU WIN!\033[0m")
                print('\033[92m', TOTAL_SCORE, '\033[0m'+'vs'+'\033[91m', ROBOT_SCORE, '\033[0m')
            else:
                print("\033[91mYOU LOSE!\033[0m")
                print('\033[91m' + str(ROBOT_SCORE), '\033[0m' +
                      'vs'+'\033[92m', str(TOTAL_SCORE), '\033[0m')

        elif userInput.lower() == 'o':
            print(LINE_SEPERATE)
            while True:
                load.ascii.titleArt()
                load.ascii.optionsArt()
                print(centered, '• Change Hand Size  [h]')
                print(centered, '• Change Rounds     [r]')
                print(centered, '• Change Difficulty [d]')
                print(centered, '• Go Back           [b]')

                optionsInput = input('\n'+centered+'           ')

                if optionsInput == 'h':
                    changeHandSize()

                elif optionsInput == 'r':
                    changeRounds()

                elif optionsInput == 'd':
                    changeDifficulty()

                elif optionsInput == 'b':
                    print(LINE_SEPERATE)
                    break

                else:
                    print(LINE_SEPERATE)
                    print(centered, '    Invalid command.')

        elif userInput.lower() == 'b':
            endGame(hands)
            break

        else:
            print(LINE_SEPERATE)
            print(centered, '    Invalid command.')
    else:  # Safe Check
        print("Something Went Wrong.", "'current' option is set to", choice)


# Start Game
if __name__ == '__main__':
    introduction()
    playGame(wordsLoaded, DIFFICULTY)
