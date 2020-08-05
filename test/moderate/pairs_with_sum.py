import unittest

from moderate.pairs_with_sum import find_pairs_with_sum


class MyTestCase(unittest.TestCase):
    def test(self):
        arr = [-4, 2, -8, 3, 7, -2]
        target = -1
        expected = [(-4, 3), (-8, 7)]
        self.assertCountEqual(expected, find_pairs_with_sum(arr, target))

    def test_no_matches(self):
        arr = [4, 5]
        target = 6
        self.assertCountEqual([], find_pairs_with_sum(arr, target))

    def test_too_short(self):
        arr = [4]
        target = 4
        self.assertCountEqual([], find_pairs_with_sum(arr, target))

    def test_repeated_elements(self):
        arr = [1, 2, 1]
        target = 3
        self.assertCountEqual([(1, 2)], find_pairs_with_sum(arr, target))


if __name__ == "__main__":
    unittest.main()
