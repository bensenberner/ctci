from unittest import TestCase

from mathemathics.intersecting_lines import Line, Point


class Test(TestCase):
    def assert_lines_intersect_at(self, l1, l2, point):
        self.assertEqual(point, l1.get_intersection_with(l2))
        self.assertEqual(point, l2.get_intersection_with(l1))

    def test_get_intersecting_point(self):
        l1 = Line(p1=Point(1, 1), p2=Point(3, 3))
        l2 = Line(p1=Point(1, 3), p2=Point(3, 1))
        self.assert_lines_intersect_at(l1, l2, Point(2, 2))

    def test_parallel_nonvertical_lines(self):
        l1 = Line(p1=Point(1, 1), p2=Point(3, 3))
        l2 = Line(p1=Point(2, 2), p2=Point(4, 4))
        self.assert_lines_intersect_at(l1, l2, None)

    def test_parallel_vertical_lines(self):
        l1 = Line(p1=Point(1, 1), p2=Point(1, 3))
        l2 = Line(p1=Point(2, 2), p2=Point(2, 8))
        self.assert_lines_intersect_at(l1, l2, None)

    def test_horizontal_line_with_sloped_line(self):
        horizontal_line = Line(p1=Point(1, 1), p2=Point(8, 1))
        sloped_line = Line(p1=Point(1, 1), p2=Point(2, 2))
        self.assert_lines_intersect_at(horizontal_line, sloped_line, Point(1, 1))

    def test_horizontal_and_vertical_line(self):
        l1 = Line(p1=Point(-5, 0), p2=Point(11, 0))
        l2 = Line(p1=Point(0, -2), p2=Point(0, 8))
        self.assert_lines_intersect_at(l1, l2, Point(0, 0))
