import unittest

from hard.jump_game_ii_45 import jump


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, jump([2, 3, 1, 1, 4]))
