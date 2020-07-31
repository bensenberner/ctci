import unittest

from moderate.contiguous_sequence import contig_seq_sum


class Test(unittest.TestCase):
    def test(self):
        arr = [2, -8, 3, -2, 4, -10] * 10
        self.assertEqual(5, contig_seq_sum(arr))

    def test_sea_of_negatives(self):
        arr = [-8, -18, -38, 5, -1, 4, -870, -32]
        self.assertEqual(8, contig_seq_sum(arr))


if __name__ == "__main__":
    unittest.main()
