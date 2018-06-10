# Hacker
# - Argenis Rodriguez

import src.const as c
import random as rd


def main():
    '''
    Hacker Game
    - Main
    '''
    level = 1
    hints = 4
    word = get_word(level)

    while(hints > 0):
        print(c._TITLE_title_text.format(level, hints))
        encryptd = encrypt(word, 1)
        print(decrypt(encryptd, word, hints))
        hints -= 1


def encrypt(word, num):
    '''
    Word Encrypter
    - Encrypts given word using any of the functions defined.
      Each function returns a different type of input working ASCII values.

        regular()       : returns the word with it's value shifted by 1 ~ 3 (random)
        backwords()     : returns the word backwords.
        ascending()     : returns the word with every other value shifted by 1.
                            ex. Hello -> Hellp || Good Day -> Good Ebz || One Morning -> One Npsokpi
        descending()    : returns the word with every other value shifted by 1 in reverse.
                            ex. Hello -> olleI || Good Day -> yaD eppH || One Morning -> gninspN gpQ

      Each function takes the alphabetical value of each letter. For instance: 'a' || 'A' : 0
                                                                               'z' || 'Z' : 25
      Then it adds the value converted back to its original letter to 'the_word'.
    '''

    def regular():
        the_word = ''

        key = rd.randint(1, 3)
        for letter in word:
            if letter.isupper():
                value = ((ord(letter) % 65) + key) % 26
                the_word += chr(value + 65)
            elif letter.islower():
                value = ((ord(letter) % 97) + key) % 26
                the_word += chr(value + 97)
            else:
                the_word += i
        return the_word

    def backwords():
        the_word = ''

        for letter in range(len(word) - 1, -1, -1):
            the_word += word[letter]
        return the_word

    def ascending():
        the_word = ''

        key = 0
        for letter in word:
            if letter.isupper():
                value = ((ord(letter) % 65) + int(key)) % 26
                the_word += chr(value + 65)
            elif letter.islower():
                value = ((ord(letter) % 97) + int(key)) % 26
                the_word += chr(value + 97)
            else:
                the_word += letter
            key += 0.25
        return the_word

    def descending():
        the_word = ''

        key = 0
        for letter in range(len(word) - 1, -1, -1):
            if word[letter].isupper():
                value = ((ord(word[letter]) % 65) + int(key)) % 26
                the_word += chr(value + 65)

            elif word[letter].islower():
                value = ((ord(word[letter]) % 97) + int(key)) % 26
                the_word += chr(value + 97)
            else:
                the_word += word[letter]

            key += 0.25

        return the_word

    '''
    Return Function
    '''
    if num is 0:
        return regular()
    elif num is 1:
        return backwords()
    elif num is 2:
        return ascending()
    elif num is 3:
        return descending()


def decrypt(encrypted, unencrypted, hints):
    '''
    Decrypt Word
    - The function takes in the encrypted version of the word,
      the unencrypted version and the number of hints the player has remaining.

      'nums[]' is a list of non-repeating random integers the length of ('hints' % c._INFO_num_hints)
        - Used for randomly selecting a value to reveal to the user utilizing the random.sample func.
          ex. [0,2,4]
              [1,3,5]
      'hints_nums[]' is a list of numbers the length of the encrypted word.
        - This will be used to get how many hints the player should receive this function.

      Then we make a copy of the encrypted word into a list.
        - This is to be able to change each index's value as we please.
      Next the function steps into a loop that runs the number of hints needed to reveal.
        (hints_nums[hints]) - | 4 : 0 | 3 : 1 | 2 : 2 |
      Each time replacing the value by a random

      Returning the joined version of the 'revealed' list.

    '''
    nums = rd.sample(range(0, len(encrypted)), c._INFO_num_hints)
    hints_nums = [i for i in range(c._INFO_num_hints, -1, -1)]

    revealed = list(encrypted)
    for hint_i in range(0, hints_nums[hints]):
        reveal_num = rd.choice(nums)
        revealed[reveal_num] = "{}".format(unencrypted[reveal_num])
        print(revealed)
    return ''.join(revealed)


def parse_word_bank():
    '''
    Parse Word Bank
    - Opens the provided file location in 'c._INFO_words_file'
      and parses each word with their first letter capitalized
      into 'loaded_words[]' then returns the list.

      O(n)
    '''
    loaded_words = []
    with open(c._INFO_words_file, 'r') as word_file:
        for line in word_file:
            loaded_words.append(line.strip().title())
    return loaded_words


def get_word(level):
    '''
    Get Word
    - Returns a word that complies with the level rules.
      If the level is less than 3, the word will always be of length 4.
      Otherwise the length of the word will be less than or equal to 7
        * To avoid insane difficulty.
      After, add the word to a list(seen[]) to avoid repetition.
    '''
    seen = []
    for word in word_bank:
        if word not in seen:
            seen.append(word)
            if level <= 3 and len(word) == 4:
                return word
            elif level >= 4 and len(word) <= 7:
                return word


word_bank = parse_word_bank()
