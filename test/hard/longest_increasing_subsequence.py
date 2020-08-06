import unittest

from hard.longest_increasing_subsequence import longest_increasing_subsequence_len


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [1, 100, 8, 150, 3, 125, 6, 120, 7, 8]
        longest_subsequence = [1, 3, 6, 7, 8]
        self.assertListEqual(
            longest_subsequence, longest_increasing_subsequence_len(arr)
        )
