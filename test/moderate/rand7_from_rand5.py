import unittest
from collections import Counter

from moderate.rand7_from_rand5 import rand7
import random


class Test(unittest.TestCase):
    def test_something(self):
        random.seed(42)
        counter = Counter()
        for _ in range(10000):
            counter[rand7()] += 1
        expected_normalized_count = 1 / 7
        for count in counter.values():
            normalized_count = count / 10000
            self.assertAlmostEqual(
                expected_normalized_count, normalized_count, places=2
            )
