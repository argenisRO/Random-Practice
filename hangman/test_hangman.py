#!/usr/bin/env python
# Hangman
# - Argenis Rodriguez

from src.body import display_current_w, correct_guess, available_letters, right_justify
import unittest


class TestHangman(unittest.TestCase):

    def setUp(self):
        self._word_bank = ['apple', 'barn', 'young', 'zebra']
        self._word_choice = self._word_bank[2]
        self._user_guess_total = '10'
        self._letters_guessed = ['y', 'l', 'e', 'o', 'd']

    def test_display_current_w(self):
        self.assertEqual(display_current_w(self._word_choice,
                                           self._letters_guessed), ' y  o  _  _  _ ')

    def test_correct_guess(self):
        self.assertTrue(correct_guess('young', self._letters_guessed, self._word_choice))
        self.assertFalse(correct_guess('l', self._letters_guessed, self._word_choice))

    def test_available_letters(self):
        self.assertEqual(available_letters(self._letters_guessed), 'abcfghijkmnpqrstuvwxz')

    def test_right_justify(self):
        test_string = 'Test Word'
        right_justified = right_justify(test_string, 20)
        self.assertEqual(right_justified, 11)


if __name__ == '__main__':
    unittest.main()
