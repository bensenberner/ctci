import unittest

from moderate.count_bits import countBits


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([0, 1, 1, 2, 1, 2], countBits(5))
        self.assertEqual([0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2], countBits(12))
