import unittest

from moderate.operations import subtract, multiply, divide


class Test(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(0, subtract(5, 5))
        self.assertEqual(0, subtract(-5, -5))
        self.assertEqual(10, subtract(5, -5))
        self.assertEqual(-10, subtract(-5, 5))

    def test_multiply(self):
        self.assertEqual(0, multiply(0, 5))
        self.assertEqual(6, multiply(2, 3))
        self.assertEqual(-6, multiply(-2, 3))
        self.assertEqual(-6, multiply(2, -3))
        self.assertEqual(6, multiply(-2, -3))

    def test_divide(self):
        self.assertEqual(0, divide(0, 5))
        with self.assertRaises(ZeroDivisionError):
            divide(4, 0)
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(0, divide(3, 6))
        self.assertEqual(1, divide(3, 3))
        self.assertEqual(-1, divide(-3, 3))
        self.assertEqual(-1, divide(3, -3))


if __name__ == "__main__":
    unittest.main()
