import copy
import unittest

from hard.shuffle import shuffle


class MyTestCase(unittest.TestCase):
    def test_something(self):
        import random

        random.seed(42)
        cards = list(range(52))
        old_cards = copy.deepcopy(cards)
        shuffle(cards)
        self.assertCountEqual(old_cards, cards)
        self.assertNotEqual(old_cards, cards)


if __name__ == "__main__":
    unittest.main()
