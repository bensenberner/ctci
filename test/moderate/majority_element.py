import unittest

from hard.majority_element import majority_element


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [1, 2, 5, 9, 5, 9, 5, 5, 5]
        self.assertEqual(5, majority_element(arr))

    def test_negations(self):
        arr = [1, 5, 2, 5, 3, 5, 4, 5, 6, 5]
        self.assertEqual(-1, majority_element(arr))


if __name__ == "__main__":
    unittest.main()
