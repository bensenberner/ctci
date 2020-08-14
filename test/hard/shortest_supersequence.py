import unittest

from hard.shortest_supersequence import shortest_supersequence


class Test(unittest.TestCase):
    def test_something(self):
        short = [1, 5, 9]
        long = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
        self.assertEqual((7, 10), shortest_supersequence(short, long))

    def test_something_else(self):
        short = [1, 5, 9]
        long = [7, 5, 9, 0, 2, 1, 3, 7, 9, 1, 1, 5, 8, 8, 9, 7]
        self.assertEqual((8, 11), shortest_supersequence(short, long))


if __name__ == "__main__":
    unittest.main()
