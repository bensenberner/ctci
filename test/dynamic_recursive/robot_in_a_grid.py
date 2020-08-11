import unittest

from dynamic_recursive.robot_in_a_grid import traverse_grid


class Test(unittest.TestCase):
    def test(self):
        grid = [
            [1, 1, 0, 1],
            [0, 1, 0, 1],
            [0, 1, 0, 1],
            [0, 1, 1, 1],
        ]
        expected_path = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
        self.assertEqual(expected_path, traverse_grid(grid))
