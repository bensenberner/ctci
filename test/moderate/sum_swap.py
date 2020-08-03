import unittest

from moderate.sum_swap import sum_swap


class Test(unittest.TestCase):
    def test(self):
        arr1 = [4, 1, 2, 1, 1, 2]
        arr2 = [3, 6, 3, 3]
        self.assertListEqual([1, 3], sum_swap(arr1, arr2))

    def test2(self):
        arr1 = [1, 2, 5, 2, 9]
        arr2 = [1, 7, 5, 7, 9]
        self.assertListEqual([2, 7], sum_swap(arr1, arr2))

    def test3(self):
        arr1 = [1, 7, 5, 7, 9]
        arr2 = [1, 2, 5, 2, 9]
        self.assertListEqual([7, 2], sum_swap(arr1, arr2))
