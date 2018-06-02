# Scrab
# - Argenis Rodriguez

from src import const as c
from random import randrange


def deal_hand():
    '''
    Deal A Hand
    - Returns a sorted list of Vowels and Consonants
      randomy placed which is the size of _INFO_hand_size.
    '''
    _hand = []
    _max_vowel = c._INFO_hand_size // 3

    for i in range(_max_vowel):
        _hand.append(c._INFO_vowels[randrange(0, len(c._INFO_vowels))])

    for i in range(_max_vowel, c._INFO_hand_size):
        _hand.append(c._INFO_consonants[randrange(0, len(c._INFO_consonants))])

    return sorted(_hand)


def word_score(word):
    '''
    Word Score
    - Returns the score of the given word. Score is calculated
      base on the values provided in _INFO_letter_values times
      the length of the word. If the user guesses a word the
      same length as the h_size, then _INFO_jackpot_score is added as extra.
    '''
    score = 0

    if len(word) == c._INFO_hand_size:
        score += c._INFO_jackpot_score

    for letter in word:
        score += c._INFO_letter_values[letter]

    return score * len(word)


def update_hand(hand, word):
    '''
    Update The Hand
    - Updates the given hand by going through each letter of
      the given word and removing it if found in hand.

    - _hand is a copy of the hand to avoid mutation
    '''
    _hand = hand[:]

    for i_word in word:
        count = 0
        for i_hand in _hand:
            if i_hand is i_word:
                _hand.remove(_hand[count])
                break
            count += 1
    return _hand


def check_validation(hand, word):
    '''
    Check Validation
    - Returns True or False if the ward is a valid word.
      First checking if the word is empty or in the word_bank
      and checking the word to be in the players _hand.
    - _hand is a copy of the hand to avoid mutation
    '''
    _hand = hand[:]

    if word is '' or word not in word_bank[word[0]]:
        return False

    for i_word in word:
        count = 0
        if i_word not in _hand:
            return False
        for i_hand in _hand:
            if i_hand is i_word:
                _hand.remove(_hand[count])
                break
            count += 1
    return True


def parse_words():
    '''
    Parse Words
    - Returns a large dictionary whos key's are all the letters of the alphabet
      and the values are list of all the words that start with the key's letter.
      The Values are sorted according to the word's length.
      * ex. {
            'b':['ben''bane','bone','banana'],
            'e':['ear','easy','evil'],
            'a':['air','apple','azure'],
            'z':['zoo','zeebra']
            }
    - O(n)
      The keys are not ordered.
    '''
    word_bank = {}

    with open(c._INFO_words_file, 'r') as word_text:
        for line in word_text:
            word = line.strip().lower()
            if word[0] not in word_bank:
                word_bank[word[0]] = []
            else:
                word_bank[word[0]].append(word)
    for words in word_bank:
        word_bank[words].sort(key=len)

    return word_bank


def get_player_input(_input):
    '''
    Retrieve User Info
    - The user is prompted for input until given a valid answer,
      then the valid answer is returned based on the _input.
        0 : Get User Integer.                  [Integer]
        1 : Get User String.                   [Regular String]
        2 : Get User Single-Character String.  [Uppercase String]
        3 : Get User Single Difficulty String. [Lowercase String]

        * text_display is saying (if _input is 0)        = num_input,
                                 (elif _input is 2 or 3) = letter_input,
                                 (else)                  = word_input
    '''
    text_display = c._USER_num_input if _input is 0 else (
        c._USER_letter_input if _input in [2, 3] else c._USER_word_input)

    while True:
        '''
        Input Check
        - Checking Int vs String cases with u_input and
          Except ValueErrors due to human error.
        '''
        try:
            u_input = int(input(text_display)) if _input is 0 else input(text_display)
        except (ValueError):
            print(c._USER_input_error)
            continue

        if _input is 0 and u_input > 0:
            return u_input

        elif _input is 1 and (u_input.isalpha() or u_input == '.') and len(u_input) >= 0:
            return u_input

        elif _input is 2 and u_input.isalpha() and len(u_input) == 1:
            return u_input.upper()

        elif _input is 3 and u_input.isalpha() and len(u_input) == 1 \
                and u_input.lower() in c._INFO_difficulty_options:
            return u_input.lower()

        print(c._USER_input_error)


def get_computer_input(_Computer_Hand):
    '''
    Get Computer's Input
    - Returns the Best Word the bot can find.
      First converts the hand to avoid duplicates, then
      for every letter in the hand, look up all the words
      in the word_bank. Checks constantly if the word is valid or not
      and then calculates if the word is the BEST word it's found.
      - Difficulty 'Easy'   : Bot only finds words with less than 3 characters.
      - Difficulty 'Meidum' : Bot only finds words with less than 5 characters.
      - Difficulty 'Hard'   : Bot will find any word with any length.

    - O(n²)
    '''
    highest_score = 0
    best_word = None

    # Converting the hand to a set to eliminate duplicates
    # So the algorithm wont have to search the same sublist.
    hand_set = set(_Computer_Hand)

    for letter in hand_set:
        for word in word_bank[letter]:
            if ((c._INFO_difficulty == 'e') and (len(word) > 2)) or \
               ((c._INFO_difficulty == 'm') and (len(word) > 4)):
                break
            elif check_validation(_Computer_Hand, word):
                score = word_score(word)
                if score > highest_score:
                    highest_score = score
                    best_word = word
    return best_word


# Parsed Word Bank
word_bank = parse_words()
