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
wLoad = load.word_load.allWords
DIFFICULTY = 'e'
DIF_CHOICE = {'e': '\033[92mEasy\033[0m', 'm': '\033[93mMedium\033[0m', 'h': '\033[91mHard\033[0m'}


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}


def loading():
    '''
    Loading Animation
    '''

    for dot in itertools.cycle(['.', '..', '...', '\x1b[2K']):
        if LOADED:
            break
        sys.stdout.write('\r' + dot)
        sys.stdout.flush()
        time.sleep(0.7)


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


def displayHand(hand, output):
    '''
    Displays the current hand to the console
    '''
    if output == 'print':
        printedHand = []
        for letter in hand:
            for j in range(hand[letter]):
                printedHand.append(letter)
        return ' '.join(printedHand)
    elif output == 'return':
        handList = []
        for letter in hand:
            for j in range(hand[letter]):
                handList.append(letter)
        return handList
    else:
        raise ValueError('Error Displaying Hand! - Hand:', hand, 'Output:', output)


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

    if userInput == '.':
        print(LINE_SEPERATE)
        print(centered, 'Round Over. Total score:', TOTAL_SCORE, 'points.\n')
    else:
        print(LINE_SEPERATE)
        print(centered, 'You ran out of letters. Total score:', TOTAL_SCORE, 'points.')


def isValidWord(word, hand):
    '''
    Returns True or False based on if 'word'
    Is valid from within 'wLoad' and is not empty.
    '''

    tempHand = hand.copy()

    if word not in wLoad[word[0]]:
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


def compChooseWord(hand, n):
    '''
    Returns the best chosen word from 'wLoad'
    for the computer player
    '''

    bestScore = 0
    bestWord = None

    for handLetter in displayHand(hand, 'return'):
        for word in wLoad[handLetter]:
            if (DIFFICULTY == 'e') and (isValidWord(word, hand)) and (len(word) <= 2) or \
               (DIFFICULTY == 'm') and (isValidWord(word, hand)) and (len(word) <= 4) or \
               (DIFFICULTY == 'h') and (isValidWord(word, hand)):
                score = getWordScore(word, n)
                if (score > bestScore):
                    bestScore = score
                    bestWord = word
    return bestWord


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
        userDifficulty = input(centered+'           ')
        if userDifficulty.lower() not in ['e', 'm', 'h', 'easy', 'medium', 'hard']:
            print(LINE_SEPERATE)
            print(centered, "     Invalid Input.")
            print(('\t'*8), "Please choose between (e), (m), and (h)")
        else:
            print(LINE_SEPERATE)
            DIFFICULTY = userDifficulty
            break


def endGame():
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
            if int(handsize) >= 1:
                print(LINE_SEPERATE)
                HAND_SIZE = int(handsize)
                print(('\t'*8), '   Successfully Changed Your Hand Size')
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
                print(('\t'*8), '   Successfully Changed Game Rounds')
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


def playHand(hand, n):
    '''
    Interactive User Player Base
    '''
    global TOTAL_SCORE
    global ROUND
    invalid = 1
    centered = '\t'*9
    print(LINE_SEPERATE)

    while calculateHandlen(hand) > 0:
        load.ascii.titleArt()
        load.ascii.yourTurn()

        print('\n'*2)
        print(centered, 'Round {}!   - {} vs {}'.format((str(ROUND)),
                                                        ('\033[92m ' + str(TOTAL_SCORE) + ' \033[0m'),
                                                        ('\033[91m ' + str(ROBOT_SCORE) + ' \033[0m')))
        print('\n')
        print(centered, "Current Hand: {}".format(displayHand(hand, 'print')))

        if invalid == 4:
            print(LINE_SEPERATE)
            print(centered, 'Moving on with the game.')
            userInput == '.'
            break

        print(centered, "Enter a word\n", centered, "[.] to finish")

        try:
            userInput = str(input(centered+'               '))
            userInput = userInput.lower()

            if userInput == '.':
                break

            elif not isValidWord(userInput, hand):
                print(LINE_SEPERATE)
                print(centered, 'Invalid word, please try again.')
                invalid += 1

            else:
                print(LINE_SEPERATE)
                invalid = 0
                copy = TOTAL_SCORE
                TOTAL_SCORE += getWordScore(userInput, n)
                added = TOTAL_SCORE - copy
                print(centered, ' "{}" earned {} points!'.format(
                    userInput, getWordScore(userInput, n)))
                print(centered, '{} Score Increased By: {}'.format(('\033[92m+\033[0m'),
                                                                   ('\033[92m' + str(added) + '\033[0m')))
                print(('\t'*10), '{} vs {}'.format(('\033[92m ' + str(TOTAL_SCORE) + ' \033[0m'),
                                                   ('\033[91m ' + str(ROBOT_SCORE) + ' \033[0m')))
                hand = updateHand(hand, userInput)
        except (KeyError):
            print(LINE_SEPERATE)
            print(centered, 'Invalid Command, please try again.')


def compPlayHand(hand, n, dif):
    '''
    Computer plays Scrabble against alone.
    '''
    global ROBOT_SCORE
    global LOADED

    centered = '\t'*9
    print(LINE_SEPERATE)

    totalScore = 0
    while (calculateHandlen(hand) > 0):
        load.ascii.titleArt()
        load.ascii.enemyTurn()

        print('\n'*2)
        print(centered, 'Round {}!   - {} vs {}'.format((str(ROUND)),
                                                        ('\033[91m ' + str(ROBOT_SCORE) + ' \033[0m'),
                                                        ('\033[92m ' + str(TOTAL_SCORE) + ' \033[0m')))
        print('\n')
        print(centered, "Current Hand: {}".format(displayHand(hand, 'print')))

        LOADED = False

        loader = threading.Thread(target=loading)
        loader.start()
        word = compChooseWord(hand, n)
        LOADED = True

        if word is None:
            break

        else:
            print(LINE_SEPERATE)
            if not isValidWord(word, hand):
                print("This... can't be happening!")
                break
            else:
                score = getWordScore(word, n)
                ROBOT_SCORE += score
                print(centered, '"{}" earned {} points. Total: {}'.format(word, score, ROBOT_SCORE))
                hand = updateHand(hand, word)
                print(centered, '{} vs {}'.format(('\033[92m ' + str(TOTAL_SCORE) + ' \033[0m'),
                                                  ('\033[91m ' + str(ROBOT_SCORE) + ' \033[0m')))


def playGame(choice):
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
                playHand(dealtH, HAND_SIZE)
                hands += 1
                print(LINE_SEPERATE)
                # Robot Turn
                dealtI = dealHand(HAND_SIZE)
                compPlayHand(dealtI, HAND_SIZE, choice)
                robotHands += 1
                print(LINE_SEPERATE)

            # End of Game
            if TOTAL_SCORE > ROBOT_SCORE:
                print(centered, "       \033[92mYOU WIN!\033[0m")
                print(centered, '     {} vs {}'.format(('\033[92m ' + str(TOTAL_SCORE) + ' \033[0m'),
                                                       ('\033[91m ' + str(ROBOT_SCORE) + ' \033[0m')))

            else:
                print(centered, "  \033[91mYOU LOSE!\033[0m")
                print(centered, ' {} vs {}'.format(('\033[91m ' + str(ROBOT_SCORE) + ' \033[0m'),
                                                   ('\033[92m ' + str(TOTAL_SCORE) + ' \033[0m')))

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
            endGame()
            break

        else:
            print(LINE_SEPERATE)
            print(centered, '    Invalid command.')
    else:  # Safe Check
        print("Something Went Wrong.", "'current' option is set to", choice)


# Start Game
if __name__ == '__main__':
    introduction()
    playGame(DIFFICULTY)
