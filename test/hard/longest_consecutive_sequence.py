import unittest

from hard.longest_consecutive_sequence import longest_consecutive_seq


class Test(unittest.TestCase):
    def test(self):
        arr = [100, 4, 200, 1, 3, 2]
        self.assertEqual(4, longest_consecutive_seq(arr))
