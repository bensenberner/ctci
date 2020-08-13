import unittest

from int.kth_largest import kth_largest


class Test(unittest.TestCase):
    def test(self):
        arr = [7, 5, 2, 7, 1, 8, 3]
        self.assertEqual(5, kth_largest(arr, 4))

    def test_simple(self):
        arr = [3, 2, 1]
        self.assertEqual(3, kth_largest(arr, 1))
        self.assertEqual(2, kth_largest(arr, 2))
