import unittest

from hard.respace import respace


class Test(unittest.TestCase):
    def test_ctci(self):
        self.assertEqual(
            ["jess", "looked", "just", "like", "tim", "her", "brother"],
            respace("jesslookedjustliketimherbrother"),
        )

    def test1(self):
        self.assertEqual(["tim", "her"], respace("timher"))

    def test2(self):
        self.assertEqual(["her", "lame", "brother"], respace("herlamebrother"))
