import unittest

from hard.first_missing_positive_41 import firstMissingPositive


class Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(3, firstMissingPositive([1, 2, 0]))
        self.assertEqual(2, firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, firstMissingPositive([7, 8, 9, 11, 12]))
