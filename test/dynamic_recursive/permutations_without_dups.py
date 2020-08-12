import unittest

from dynamic_recursive.permutations_without_dups import perms_without_dups


class Test(unittest.TestCase):
    def test(self):
        expected = ["abc", "acb", "bac", "bca", "cab", "cba"]
        self.assertCountEqual(expected, perms_without_dups("abc"))


if __name__ == "__main__":
    unittest.main()
