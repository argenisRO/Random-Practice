#!/usr/bin/env python
# Hacker
# - Argenis Rodriguez

from src.body import encrypt
import unittest


class TestScrab(unittest.TestCase):

    def test_encrypt(self):
        self.assertIn(encrypt('hello', 0), ['ifmmp', 'jgnnq', 'khoor'])
        self.assertEquals(encrypt('hello', 1), )


if __name__ == '__main__':
    unittest.main()
