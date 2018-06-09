# Hangman
# - Argenis Rodriguez

import src.const as c
import random as rd
import string as st


def main():
    '''
    Hangman
    - Start the game by asking the player for input
      on the number of guesses for the game.
      - '_word_bank'        : List of the word bank
      - '_word_choice'      : A Random word from ('_word_bank')
      - '_user_guess_total' : Users choice of guesses
    '''
    # Fetched Variables
    _word_bank = word_bank(_word_file)
    _word_choice = random_word(_word_bank)
    _letters_guessed = []

    # Prompt User for Input #Guess Number
    _user_guess_total = get_user_guess()

    # Guessing Letter
    print(c._TITLE_guess_word.format(len(_word_choice)))

    # Initiate Game
    while True:
        '''
        Interactive Game
        - First checks if the number of guesses is 0
          then the game will end, if not then carry out
          with asking the user for input and checking
          if the word is correct. If the user guesses
          incorrectly, 1 is reduced from (_user_guess_total)
          and it'll continue until the user is out of guesses.
          All words that are not duplicates will be added to ['_letters_guessed']
          - '_user_guess_total'    : users number of guesses
          - '_available_letters'   : the available letters the user can choose from
          - '_user_guessed_letter' : user's prompted input to guess the word
          - '_displayed_word'      : encrypted version of ('_word_choice') base on ('_letters_guessed')
          - '_word_choice'         : A Random word from ('_word_bank')
          - '_user_guess_total'    : Users choice of guesses
        '''
        if _user_guess_total is 0:
            break
        print(c._TITLE_guesses_left.format(_user_guess_total))
        print(c._TITLE_available_left.format(available_letters(_letters_guessed)))

    # Prompt for User Input #Guess
        _user_guessed_letter = get_user_input()

        '''
        Check Correctness
        - Checks if the users guessed letter for correctness.
          - If the guessed letter is in ['_letters_guessed'],
            return the 'display_current_w' and align it with 'right_justify'.
          - If the guessed letter is 'correct_guess'(which returns true or false)
            if the word is not in _letters_guessed & is in _word_choice.
          - * 'c._user_guess_repeat[:-8]' is sliced to not raise any errors
              with Pythons string.format() function where it doesn't accept
              repeated '=' alignments into the function.
        '''
        if _user_guessed_letter in _letters_guessed:
            print(c._USER_guess_repeat.format(display_current_w(_word_choice, _letters_guessed),
                                              (right_justify(c._USER_guess_repeat[:-8], c._INFO_pos_justify))))
        elif correct_guess(_user_guessed_letter, _letters_guessed, _word_choice):
            _letters_guessed.append(_user_guessed_letter)
            print(c._USER_guess_correct.format(display_current_w(_word_choice, _letters_guessed),
                                               (right_justify(c._USER_guess_correct[:-8], c._INFO_pos_justify))))
        else:
            _letters_guessed.append(_user_guessed_letter)
            print(c._USER_guess_wrong.format(display_current_w(_word_choice, _letters_guessed),
                                             (right_justify(c._USER_guess_wrong[:-8], c._INFO_pos_justify))))
            _user_guess_total -= 1

    # End Game
    '''
    End The Game
    - Finishes the game notifying the user if they won or lost,
      Then displays the hidden word.
    '''
    if (display_current_w(_word_choice, _letters_guessed)) is _word_choice:
        print(c._TITLE_win)
        print(c._TITLE_word.format(_word_choice))
    else:
        print(c._TITLE_lose)
        print(c._TITLE_word.format(_word_choice))

    # Exit Module


def get_user_guess():
    '''
    Retrieve User Guess Number
    - Returns the users guess number as a 'int'.
      The Function will keep asking until a
      valid positive number is entered.
    '''
    while True:
        _user_guess_total = input(c._USER_guess_input)
        if _user_guess_total.isdigit() and int(_user_guess_total) > 0:
            return int(_user_guess_total)
        else:
            print(c._USER_guess_error)


def get_user_input():
    '''
    Retrieve User Input
    - Returns the users guessed letter making sure
      the length is 1 and the type is a string.
    '''
    while True:
        _user_input = input(c._USER_guess_letter)
        if len(_user_input) is 1 and type(_user_input) is str:
            return _user_input
        else:
            print(c._USER_guess_error)


def display_current_w(_word_choice, _letters_guessed):
    '''
    Decoder
    - Returns the ('_word_choice') decoded base on
      the currently guessed letters.
      - '_word_choice'      : A Random word from ('_word_bank')
    '''
    _decoded = ''
    for _letter in _word_choice:
        if _letter in _letters_guessed:
            # - Format is used here to easily apply spaces
            #   between the guessed letter
            _decoded += ' {} '.format(_letter)
        else:
            _decoded += ' _ '
    return _decoded


def correct_guess(_user_guess, _letters_guessed, _word_choice):
    '''
    True/False Guess
    - Returns 'True' if the guess
      was correct 'False' otherwise.
      - '_word_choice'      : A Random word from ('_word_bank')
    '''
    if _user_guess in _word_choice and _user_guess not in _letters_guessed:
        return True
    return False


def available_letters(_letters_guessed):
    '''
    Available Letters View
    - Returns all the letters the user is still
      allowed to use throughout the game.
      - _alpha_letters : A list of the alphabet
        (A - Z) from the 'String' module.

      - '_letters_guessed' : All the letters guessed
        by the user so far.
    '''
    _alpha_letters = list(st.ascii_lowercase)
    for _letter in _letters_guessed:
        if _letter in _alpha_letters:
            _alpha_letters.remove(_letter)
    return ''.join(_alpha_letters)


def word_bank(_word_file):
    '''
    Word Bank Loader
    - Packs all the words from the word bank into
      a list from the provided TXT file.
    '''
    _loaded_words = []
    with open(c._INFO_words_file, 'r') as word_file:
        for line in word_file:
            _loaded_words.append(line.strip().lower())
    return _loaded_words


def random_word(_wordbank):
    '''
    Random Word Chooser
    - Returns a random word from the provided ('_wordbank')
      list using the 'Random'(rd) Module.
      - _wordbank:   list:Strings
    '''
    return rd.choice(_wordbank)


def right_justify(text_string, pos):
    '''
    Right Justifier
    - Takes the given positional number ('_INFO_pos_justify')
      and substracts it from the length of the text given.
      Returning the number of spaces needed to perfectly align each string.
    '''
    return (pos - len(text_string))
