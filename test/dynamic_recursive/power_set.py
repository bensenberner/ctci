import unittest

from dynamic_recursive.power_set import power_set


class Test(unittest.TestCase):
    def test_0(self):
        self.assertCountEqual([set()], power_set(set()))

    def test_2(self):
        expected = [set(), {1}, {2}, {1, 2}]
        self.assertCountEqual(expected, power_set({1, 2}))

    def test_3(self):
        expected = [set(), {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 3}, {1, 2, 3}]
        self.assertCountEqual(expected, power_set({1, 2, 3}))
