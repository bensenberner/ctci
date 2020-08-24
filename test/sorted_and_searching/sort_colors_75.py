import unittest

from sorting_searching.sort_colors_75 import sort_colors


class Test(unittest.TestCase):
    def test_lc(self):
        colors = [2, 0, 2, 1, 1, 0]
        sort_colors(colors)
        self.assertEqual([0, 0, 1, 1, 2, 2], colors)

    def test_2(self):
        colors = [2, 2, 1, 1, 0, 0]
        sort_colors(colors)
        self.assertEqual([0, 0, 1, 1, 2, 2], colors)

    def test_3(self):
        colors = [1, 0]
        sort_colors(colors)
        self.assertEqual([0, 1], colors)
