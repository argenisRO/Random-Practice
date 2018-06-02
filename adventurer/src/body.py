# Adventurer
# - Argenis Rodriguez

import src.const as c
import src.data as data
import src.helper as hp


def main():
    '''
    Main Game Function (start)
    - Begins the game introducing the player
      to the character creator asking for input
      on the following variables
        - Name:   playerName     input:String
        - Sex:    sex            input:String
        - Height: height         input:Float
        - Class:  class_select   input:String
    '''
    # Character Creator
    print(c._title_create_char)
    _playerName = input(c._id_name_input)
    _sex = input(c._id_sex_input)
    _height = input(c._id_height_input)
    _class = class_select()

    # Player Class Creation
    Player_1 = data.Player(_playerName, _sex, _height, _class)

    # Player Class Info Confirmation
    print(c._id_creation_complete.format(Player_1.get_name(),
                                         Player_1.get_class_dialog()))


def class_select():
    ''' '
    '
    Player Class Selection
    - Player is asked to pick a class from
      the (get_available_classes) variable.
    '''
    print(c._title_class_select)

    while True:
        _class_input = input(c._id_class_input)
        if _class_input.lower() not in hp.get_available_classes():
            print(c._message_input_error)
        else:
            return _class_input


def eMsg():
    '''
    End Game Message
    -  Ends the game and thanks the player for playing.
    '''
    print(c._title_end_game)
