# Scrab
# - Argenis Rodriguez

from src import const as c
from src.info import *


def main():
    # Introductory Choosing Difficulty
    _INTRO_display_difficulty()
    c._INFO_difficulty = get_player_input(3)

    # Menu Selection
    print(c._TITLE_menu_title)
    _MAIN_MENU_()

    # End Game
    _END_SCREEN_()


def _MAIN_MENU_():
    '''
    Menu Selection
    - Main Menu of The Game

      . Start
      . Options
      . End Game
    '''
    while True:
        _INTRO_display_title_screen()
        user_selection = get_player_input(2)
        if user_selection == 'S':
            _START_GAME_()
        elif user_selection == 'O':
            print('entered options')
            _OPTIONS_()
        elif user_selection == 'B':
            break
        else:
            print(c._USER_input_error)


def _START_GAME_():
    '''
    Start Game
    - Runs a while loop that will keep going until the number
      of rounds is higher than the _INFO_max_rounds rounds.
      Each player (the computer and player) deal a new hand (deal_hand())
      and run their turn functions _PLAYER_TURN_,_COMPUTER_TURN_.
      The user is told about the outcome of the match after.
    '''
    round = 0
    while round < c._INFO_max_rounds:
        round += 1

        # Player's Turn
        _Player_Hand = deal_hand()
        _PLAYER_TURN_(_Player_Hand)
        # Computer's Turn
        _Computer_Hand = deal_hand()
        _COMPUTER_TURN_(_Computer_Hand)

    if c._INFO_player_score == c._INFO_computer_score:
        print("It's a Tie!")
    elif c._INFO_player_score > c._INFO_computer_score:
        print('You Won!')
    else:
        print('You Lost!')


def _PLAYER_TURN_(_Player_Hand):
    '''
    Player's Turn
    - Players turn at the Scrab game. The player is to
      enter a word matching their _Player_Hand. If the
      player chooses to end their turn early, they would
      use the '.' character. Each time the player attempts
      to input a word, the word will run through check_validation
      and then finally the players score will be stored.
    '''
    print(c._TITLE_player_turn)
    while len(_Player_Hand) > 0:
        print(c._TITLE_current_hand.format(' '.join(_Player_Hand)))

        player_input = get_player_input(1)

        if player_input == '.':
            break

        if check_validation(_Player_Hand, player_input):
            _word_score = word_score(player_input)
            c._INFO_player_score += _word_score
            print(c._USER_valid_word.format(player_input, _word_score, c._INFO_player_score))
            _Player_Hand = update_hand(_Player_Hand, player_input)

        else:
            print(c._USER_invalid_word)


def _COMPUTER_TURN_(_Computer_Hand):
    '''
    Computer's Turn
    - The computer will attempt to get a high score word from get_computer_input.
      If the word chosen is a vlid word, the bot will use it as it's input and this
      will follow the same rules as the _PLAYER_TURN_ function.

    - If a word were to be invalid, something has gone wrong. That shouldn't happen~
    '''
    print(c._TITLE_computer_turn)
    while len(_Computer_Hand) > 0:
        print(c._TITLE_current_hand.format(' '.join(_Computer_Hand)))

        computer_input = get_computer_input(_Computer_Hand)

        if computer_input is None:
            break

        if check_validation(_Computer_Hand, computer_input):
            _word_score = word_score(computer_input)
            c._INFO_computer_score += _word_score
            print(c._USER_valid_word.format(computer_input, _word_score, c._INFO_computer_score))
            _Computer_Hand = update_hand(_Computer_Hand, computer_input)

        else:
            raise ValueError('Bot found an invalid word:', computer_input)


def _OPTIONS_():
    '''
    Menu Options
    - User is given the choice to choose which menu to activate.

      . Change Hand Size
      . Change Rounds
      . Change Difficulty
      . Go Back
    '''
    while True:
        print(c._TITLE_menu_options)
        _INFO_options_input = get_player_input(2)

        if _INFO_options_input == 'H':
            _CHANGE_SETTING_(_INFO_options_input)
        elif _INFO_options_input == 'R':
            _CHANGE_SETTING_(_INFO_options_input)
        elif _INFO_options_input == 'D':
            _CHANGE_SETTING_(_INFO_options_input)
        elif _INFO_options_input == 'B':
            break
        else:
            print(c._USER_input_error)


def _CHANGE_SETTING_(setting):
    '''
    Settings Adjuster
    - Takes the setting argument for determining which part
      of the settings the user would like to change in the const module.
        h : To change the '_INFO_hand_size' variable.
        r : To change the '_INFO_max_rounds' variable.
        d : To change the '_INFO_difficulty' variable.
    '''
    if setting == 'H':
        print(c._TITLE_menu_change.format(c._TITLE_menu_change_title[setting],
                                          c._INFO_hand_size))
        c._INFO_hand_size = get_player_input(0)

    elif setting == 'R':
        print(c._TITLE_menu_change.format(c._TITLE_menu_change_title[setting],
                                          c._INFO_max_rounds))

        c._INFO_max_rounds = get_player_input(0)

    elif setting == 'D':
        print(c._TITLE_menu_change.format(
              c._TITLE_menu_change_title[setting],
              c._INFO_difficulty_options[c._INFO_difficulty]))
        c._INFO_difficulty = get_player_input(3)

    else:
        raise ValueError("_CHANGE_SETTING_() function received",
                         setting, "as it's setting, Which is not in", c._TITLE_menu_change_title)

    print(c._TITLE_successful_change)


def _INTRO_display_difficulty():
    print(c._TITLE_intro_difficulty.format(
          c._INFO_difficulty_options['e'],
          c._INFO_difficulty_options['m'],
          c._INFO_difficulty_options['h']))


def _INTRO_display_title_screen():
    print(c._TITLE_menu_selection)


def _END_SCREEN_():
    '''
    Dismiss End Screen
    - Dismiss the player with information about the rounds played.
    '''
    print(c._TITLE_end_title.format(c._INFO_player_score, c._INFO_computer_score))


if __name__ == '__main__':
    main()
