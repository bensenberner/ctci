import unittest

from dynamic_recursive.recursive_multiply import recursive_multiply


class Test(unittest.TestCase):
    def test(self):
        # self.assertEqual(6, recursive_multiply(3, 2))
        # self.assertEqual(6, recursive_multiply(2, 3))
        self.assertEqual(72, recursive_multiply(8, 9))
