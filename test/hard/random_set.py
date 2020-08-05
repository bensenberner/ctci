import unittest

from hard.random_set import random_set


class MyTestCase(unittest.TestCase):
    def test_something(self):
        import random

        random.seed(42)
        arr = [92, 4, 81, 33]
        randset = random_set(arr, 2)
        self.assertEqual({33, 92}, randset)


if __name__ == "__main__":
    unittest.main()
