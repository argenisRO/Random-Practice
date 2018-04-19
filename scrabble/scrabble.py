# Scrabble Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed


import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = random.randrange(5, 16)
TOTAL_SCORE = 0
ROBOT_SCORE = 0
WORD_FILE = "words.txt"
LINE_SEPERATE = "\n__________________________________"
OPTION_LIST = ['u', 'c', 'only Me', 'me', 'computer ai', 'computer']

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}


def loadWords():
    '''
    Loads the words from the file into (wordsLoaded)
    '''
    inFile = open(WORD_FILE, 'r')
    wordsLoaded = []
    for line in inFile:
        wordsLoaded.append(line.strip().lower())
    print(len(wordsLoaded), "words loaded.")
    return wordsLoaded


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
    if word not in wordsLoaded:
        return False

    for e in word:
        if e not in hand:
            return False
        else:
            stored = tempHand.get(e)
            tempHand[e] = stored - 1
            if tempHand[e] < 0:
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
    while calculateHandlen(hand) > 0:
        print("\nCurrent Hand: ", end=' ')
        displayHand(hand)
        userInput = input('Enter a word ([.] to finish): ')

        if userInput == '.':
            break
        elif not isValidWord(userInput, hand, wordsLoaded):
            print('Invalid word, please try again.', LINE_SEPERATE)

        else:
            copy = TOTAL_SCORE
            TOTAL_SCORE += getWordScore(userInput, n)
            added = TOTAL_SCORE - copy
            print('"', userInput, '"', 'earned',
                  getWordScore(userInput, n), 'points', LINE_SEPERATE)
            print(' \033[92m+\033[0m Total Score Increased By: \033[92m{}\033[0m'.format(added))
            hand = updateHand(hand, userInput)

    if userInput == '.':
        print('Round Over. Total score:', TOTAL_SCORE, 'points.\n')
    else:
        print('You ran out of letters. Total score:', TOTAL_SCORE, 'points.')


def compChooseWord(hand, wordsLoaded, n):
    '''
    Returns the best chosen word from 'wordsLoaded'
    for the computer player
    '''
    bestScore = 0
    bestWord = None
    for word in wordsLoaded:
        if isValidWord(word, hand, wordsLoaded):
            score = getWordScore(word, n)
            if (score > bestScore):
                bestScore = score
                bestWord = word
    return bestWord


def compPlayHand(hand, wordsLoaded, n):
    '''
    Computer plays Scrabble against alone.
    '''
    # TODO: Optimize Speed On Word Search
    global ROBOT_SCORE
    totalScore = 0
    while (calculateHandlen(hand) > 0):

        print("\nCurrent Hand: ", end=' ')
        displayHand(hand)

        word = compChooseWord(hand, wordsLoaded, n)
        if word == None:
            break

        else:
            if (not isValidWord(word, hand, wordsLoaded)):
                print("This... shouldn't be happening.")
                break
            else:
                score = getWordScore(word, n)
                ROBOT_SCORE += score
                print('"' + word + '" earned ' + str(score) +
                      ' points. Total: ' + str(ROBOT_SCORE) + ' points', LINE_SEPERATE)
                hand = updateHand(hand, word)
                print()
    print('Total score: ' + str(ROBOT_SCORE) + ' points.\n')


def whoisPlaying():
    print('\tScrabble', LINE_SEPERATE, '\nWho will be playing?',
          '\n• Only Me     [u]',
          '\n• Computer AI [c]')

    while True:
        player = input()
        if player.lower() not in ['u', 'c']:
            print("Invalid Input. Please choose between (u) or (c)", end='\n')
        else:
            print(LINE_SEPERATE)
            return player


def changeHandSize():
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


def endGame(hands, replayed, user):
    if user == 'computer':
        print('Thanks for... beep playing!')
        print('Total Score:', ROBOT_SCORE)
    elif user == 'user':
        print('Thanks for playing!')
        print('Total Score:', TOTAL_SCORE)
    print('Total Hands Played:', hands)
    print('Total Replayed Hands:', replayed)


def confirmReplay():
    print('\nReplaying your last hand will reduce you points by 70%.')
    while True:
        userInput = input("Are you sure you want to continue? [y/n]")
        if userInput.lower() == 'y':
            return True
        elif userInput.lower() == 'n':
            return False
        else:
            continue


def playGame(wordsLoaded, choice):
    '''
    Scrabble Game
    '''
    # __Variables__
    global TOTAL_SCORE
    global ROBOT_SCORE
    global HAND_SIZE
    stored = {}
    robotStored = {}
    hands, replayedHands = 0, 0
    robotHands, replayedRobotHands = 0, 0

    # _____________

    print('\nWelcome to the Scrabble Game!', '\nHand Size:',
          HAND_SIZE, LINE_SEPERATE, '\nChoose your move\n')
    while True:

        # Robot Code
        if choice == 'c':
            print(LINE_SEPERATE, '\n\t_Computer Player_')
            print('Current Score = TOTAL_SCORE ... woops, this should not be here.', ROBOT_SCORE)
            print('\n• Deal A New Hand     [n]',
                  '\n• Replay Last Hand    [r]',
                  '\n• Change Hand Size    [h]',
                  '\n• Swap To Player Mode [s]',
                  '\n• End Game            [e]')
            userInput = input()
            if userInput.lower() == 'n':
                dealtH = dealHand(HAND_SIZE)
                compPlayHand(dealtH, wordsLoaded, HAND_SIZE)
                robotStored = dealtH
                robotHands += 1

            elif userInput.lower() == 'r':
                if bool(robotStored) == False:
                    print("\nYou have no-- I mean I have not played a hand yet.... boop beep ")
                    continue
                else:
                    compPlayHand(robotStored, wordsLoaded, HAND_SIZE)
                    replayedRobotHands += 1

            elif userInput.lower() == 'h':
                changeHandSize()

            elif userInput.lower() == 's':
                print('\nNow in Human Mode')
                choice = 'u'
                continue

            elif userInput.lower() == 'e':
                endGame(robotHands, replayedRobotHands, 'computer')
                break
            else:
                print('Invalid command... Beep..Boop')

        # Human Code
        elif choice == 'u':
            print(LINE_SEPERATE, '\n\t  _Human Player_')
            print('Current Score:', TOTAL_SCORE)
            print('\n• Deal A New Hand     [n]',
                  '\n• Replay Last Hand    [r]',
                  '\n• Change Hand Size    [h]',
                  '\n• Swap To Computer AI [s]',
                  '\n• End Game            [e]')
            userInput = input()
            if userInput.lower() == 'n':
                dealtH = dealHand(HAND_SIZE)
                playHand(dealtH, wordsLoaded, HAND_SIZE)
                stored = dealtH
                hands += 1

            elif userInput.lower() == 'r':
                if bool(stored) == False:
                    print("You have not played a hand yet.")
                    continue
                else:
                    if confirmReplay():
                        copy = TOTAL_SCORE
                        TOTAL_SCORE -= int(TOTAL_SCORE * 0.7)
                        reduction = copy - TOTAL_SCORE
                        print(
                            ' \033[91m-\033[0m Total Score Reduced By: \033[91m{}\033[0m'.format(reduction))
                        playHand(stored, wordsLoaded, HAND_SIZE)
                        replayedHands += 1
                    else:
                        continue

            elif userInput.lower() == 'h':
                changeHandSize()

            elif userInput.lower() == 's':
                print('\nNow in Computer AI mode')
                choice = 'c'
                continue

            elif userInput.lower() == 'e':
                endGame(hands, replayedHands, 'user')
                break

            else:
                print('Invalid command.')
        else:  # Safe Check
            print("Something Went Wrong.", "'current' option is set to", choice)


# Start Game
if __name__ == '__main__':
    wordsLoaded = loadWords()
    player = whoisPlaying()
    playGame(wordsLoaded, player)
