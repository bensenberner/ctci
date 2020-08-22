import unittest

from hard.count_of_smaller_nums_after_self_315 import countSmaller


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [5, 2, 6, 1]
        expected = [2, 1, 1, 0]
        self.assertEqual(expected, countSmaller(nums))

    def test_negatives(self):
        nums = [-1, -1]
        expected = [0, 0]
        self.assertEqual(expected, countSmaller(nums))

    def test_201(self):
        nums = [2, 0, 1]
        expected = [2, 0, 0]
        self.assertEqual(expected, countSmaller(nums))
