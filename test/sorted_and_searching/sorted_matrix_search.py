import unittest

from sorting_searching.sorted_matrix_search import find_element


class Test(unittest.TestCase):
    # TODO: do rectangles
    def test(self):
        matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.assertEqual((1, 0), find_element(matrix, 3))
        self.assertEqual((-1, -1), find_element(matrix, 11))
        self.assertEqual((1, 1), find_element(matrix, 4))
