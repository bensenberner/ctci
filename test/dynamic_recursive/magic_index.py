import unittest

from dynamic_recursive.magic_index import magic_index


class Test(unittest.TestCase):
    def test_first_mid(self):
        arr = [-1, 0, 2, 4, 5, 7]
        self.assertEqual(2, magic_index(arr))

    def test_min(self):
        arr = [0, 2, 4, 7, 9]
        self.assertEqual(0, magic_index(arr))

    def test_max(self):
        arr = [-1, 1]
        self.assertEqual(1, magic_index(arr))

    def test_single_element_no_luck(self):
        arr = [3]
        self.assertEqual(-1, magic_index(arr))

    def test_repeated_element(self):
        arr = [-5, -3, -2, -2, -2, -2, 7, 7, 7, 8]
        self.assertEqual(7, magic_index(arr))

    def test_all_magic(self):
        arr = list(range(100))
        self.assertEqual(49, magic_index(arr))


if __name__ == "__main__":
    unittest.main()
