from unittest import TestCase

from moderate.smallest_diff import find_smallest_diff


class Test(TestCase):
    def test_book_example(self):
        l1 = [1, 3, 14, 11, 2]
        l2 = [23, 127, 235, 19, 8]
        self.assertEqual(3, find_smallest_diff(l1, l2))

    def test_share_a_number(self):
        l1 = [1, 3, 14, 19, 2]
        l2 = [23, 127, 235, 19, 8]
        self.assertEqual(0, find_smallest_diff(l1, l2))

    def test_smallest_diff_goes_off_the_bottom(self):
        l1 = [-58, 3, 14, 11, 2]
        l2 = [23, 127, 235, 19, -59]
        self.assertEqual(1, find_smallest_diff(l1, l2))

    def test_smallest_diff_goes_off_the_top(self):
        l1 = [1, 3, 14, 111, 2]
        l2 = [23, 127, 235, 19, 113]
        self.assertEqual(2, find_smallest_diff(l1, l2))
