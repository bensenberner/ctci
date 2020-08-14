import unittest

from hard.longest_increasing_path_in_matrix_329 import longest_increasing_path


class Test(unittest.TestCase):
    def test_1(self):
        """
        The longest increasing path is [1, 2, 6, 9].
        """
        nums = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
        self.assertEqual(4, longest_increasing_path(nums))

    def test_2(self):
        """
        The longest increasing path is [3, 4, 5, 6].
        Moving diagonally is not allowed.
        """
        nums = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
        self.assertEqual(4, longest_increasing_path(nums))
