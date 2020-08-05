from unittest import TestCase

from hard.letters_and_numbers import find_largest_subarray_len_of_equal_alphanum


class Test(TestCase):
    def test(self):
        arr = ["a", "a", "a", "1", "a", "1", "1", "a", "a", "a", "a", "1", "a", "1"]
        self.assertEqual(6, find_largest_subarray_len_of_equal_alphanum(arr))
