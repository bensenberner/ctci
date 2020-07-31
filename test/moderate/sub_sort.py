from unittest import TestCase

from moderate.sub_sort import find_sub_sort_indexes


class Test(TestCase):
    def test_basic(self):
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        expected = (3, 9)
        self.assertEqual(expected, find_sub_sort_indexes(arr))

    def test_empty(self):
        self.assertEqual((0, 0), find_sub_sort_indexes([]))

    def test_one_element(self):
        self.assertEqual((0, 0), find_sub_sort_indexes([1]))

    def test_sorted_already(self):
        self.assertEqual((0, 0), find_sub_sort_indexes([1, 2, 3]))

    def test_reversed(self):
        self.assertEqual((0, 2), find_sub_sort_indexes([3, 2, 1]))
