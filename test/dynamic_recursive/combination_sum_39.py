import unittest

from dynamic_recursive.combination_sum_39 import combinationSum


class Test(unittest.TestCase):
    def test(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[7], [2, 2, 3]]
        self.assertCountEqual(expected, combinationSum(candidates, target))
