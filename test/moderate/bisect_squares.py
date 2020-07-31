from unittest import TestCase

from moderate.bisect_squares import Square, Point, find_bisection_line, Line


class Test(TestCase):
    def test_slanted_line(self):
        sq1 = Square(top_left=Point(0, 2), length=1)
        sq2 = Square(top_left=Point(0, 2), length=2)
        line = find_bisection_line(sq1, sq2)
        expected = Line(slope=-1, y_or_x_intercept=2)
        self.assertEqual(expected, line)

    def test_horizontal_line(self):
        sq1 = Square(top_left=Point(0, 2), length=2)
        sq2 = Square(top_left=Point(8, 2), length=2)
        line = find_bisection_line(sq1, sq2)
        expected = Line(slope=0, y_or_x_intercept=1)
        self.assertEqual(expected, line)

    def test_vertical_line(self):
        sq1 = Square(top_left=Point(2, 4), length=2)
        sq2 = Square(top_left=Point(1, 1), length=4)
        line = find_bisection_line(sq1, sq2)
        expected = Line(slope=None, y_or_x_intercept=3)
        self.assertEqual(expected, line)

    def test_same_square(self):
        sq1 = Square(top_left=Point(0, 2), length=2)
        sq2 = Square(top_left=Point(0, 2), length=2)
        line = find_bisection_line(sq1, sq2)
        expected = Line(slope=None, y_or_x_intercept=1)
        self.assertEqual(expected, line)

    def test_same_middle_different_square(self):
        sq1 = Square(top_left=Point(0, 2), length=4)
        sq2 = Square(top_left=Point(1, 1), length=2)
        line = find_bisection_line(sq1, sq2)
        expected = Line(slope=None, y_or_x_intercept=2)
        self.assertEqual(expected, line)
