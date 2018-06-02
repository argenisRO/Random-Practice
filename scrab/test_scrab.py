#!/usr/bin/env python
# Scrab
# - Argenis Rodriguez

from src.body import *
import unittest
from string import ascii_lowercase as alph


class TestScrab(unittest.TestCase):

    def test_word_score(self):
        # Regular Test
        self.assertEqual(word_score('james'), 70)
        # Jackpot Test
        self.assertEqual(word_score('understand'), 120)
        # Empty Test
        self.assertEqual(word_score(''), 0)

    def test_update_hand(self):
        # Regular Test
        self.assertEqual(update_hand(['a', 'b', 'c', 'd', 'e'], 'bed'), ['a', 'c'])
        # Duplicates Test
        self.assertEqual(update_hand(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 's', 'v', 'w'], 'bowl'),
                         ['a', 'c', 'd', 'e', 'f', 'g', 'j', 'm', 'n', 'p', 'q', 's', 'v'])
        # Empty Hand Test
        self.assertEqual(update_hand([], 'bed'), [])
        # Empty Word Test
        self.assertEqual(update_hand(['a', 'b', 'c'], ''), ['a', 'b', 'c'])

    def test_parse_words(self):
        '''
        Checking if all the keys are filled with all the alphabet letters.
        Also checks if the values are not None
        '''
        test_parse = word_bank
        for letter in alph:
            self.assertIn(letter, test_parse)
            self.assertIsNotNone(test_parse[letter])

    def test_check_validation(self):
        # Regular Test True
        self.assertTrue(check_validation(
            ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'i', 't', 'e', 'm', 'z'], 'itemize'))
        # Regular Test False
        self.assertFalse(check_validation(['a', 'b', 'c', 'd', 'e', 'f'], 'dine'))
        # Duplicate Test True
        self.assertTrue(check_validation(
            ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'n', 'n', 'o', 'n'], 'banana'))
        # Duplicate Test False
        self.assertFalse(check_validation(
            ['r', 'r', 'n', 'n', 'o', 'n'], 'banana'))
        # Empty Hand Test
        self.assertFalse(check_validation([], 'banana'))
        # Empty Word Test
        self.assertFalse(check_validation(['r', 'r', 'n', 'n', 'o', 'n'], ''))
        # Both Empty Test
        self.assertFalse(check_validation([], ''))

    def get_user_input(self):
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
