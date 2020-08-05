import unittest

from hard.baby_names import baby_name_sums


class MyTestCase(unittest.TestCase):
    def test(self):
        import random

        random.seed(42)
        names = {"John": 15, "Jon": 12, "Chris": 13, "Kris": 4, "Christopher": 19}
        synonyms = [
            ("John", "Jon"),
            ("John", "Johnny"),
            ("Chris", "Kris"),
            ("Chris", "Christopher"),
        ]
        result = baby_name_sums(names, synonyms)
        self.assertEqual(2, len(result))
        john_count = result.get("John", result.get("Jon", result.get("Johnny")))
        self.assertEqual(27, john_count)
        john_count = result.get("Chris", result.get("Christopher", result.get("Kris")))
        self.assertEqual(36, john_count)
