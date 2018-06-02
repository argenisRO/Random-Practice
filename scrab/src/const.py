# Scrab
# - Argenis Rodriguez

# Titles
_TITLE_menu_title = "(_ Scrab _)"
_TITLE_menu_change = "Change Setting For {}. Currently: {}"
_TITLE_menu_options = "• Change Hand Size  [h]\n• Change Rounds     [r]\n• Change Difficulty [d]\n• Go Back           [b]"
_TITLE_menu_selection = "• Start Game      [s]\n• Options         [o]\n• End Game        [b]"
_TITLE_intro_difficulty = "Choose Difficulty: {} - {} - {}"
_TITLE_menu_change_title = {'H': 'Hand Size', 'R': 'Max Rounds', 'D': 'Difficulty'}
_TITLE_successful_change = "Successfully Changed Setting.\n"
_TITLE_current_hand = "Current Hand: {}\n"
_TITLE_end_title = "\nThanks for playing!\n \033[92m{}\033[0m vs \033[93m{}\033[0m "
_TITLE_player_turn = "_Your Turn_"
_TITLE_computer_turn = "_Computers Turn_"


# Data Information
_INFO_vowels = "aeiou"
_INFO_hand_size = 8
_INFO_max_rounds = 2
_INFO_consonants = "bcdfghjklmnpqrstvwxyz"
_INFO_words_file = "../words.txt"
_INFO_difficulty = "h"
_INFO_player_score = 0
_INFO_jackpot_score = 35
_INFO_letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
    'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
_INFO_computer_score = 0
_INFO_difficulty_options = {'e': 'Easy', 'm': 'Medium', 'h': 'Hard'}

# User Messages
_USER_num_input = "Enter a Number: \n"
_USER_word_input = "Enter a Word: \n"
_USER_input_error = "Please Try Again\n"
_USER_letter_input = "Enter a Letter: \n"
_USER_invalid_word = "_Not a valid word_\n"
_USER_valid_word = "'{}' earned \033[92m{}\033[0m points!\nTotal Score: \033[92m{}\033[0m\n"
