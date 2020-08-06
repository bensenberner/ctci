import unittest

from hard.kth_multiple import kth_multiple


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected_nums = [1, 3, 5, 7, 9, 15, 21, 25, 27]
        for _idx, expected_num in enumerate(expected_nums):
            k = _idx + 1  # ordinal number, not python idx
            self.assertEqual(expected_num, kth_multiple(k))


if __name__ == "__main__":
    unittest.main()
