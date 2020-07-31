"""
Given two squares on a two dimensional plane, find a line that would cut these two squares in half.
Assume that the top and bottom sides of the square run parallel to the x-axis.
---------------------
three numbers define a square:
(x, y) of the top left corner
s, the length of the side

dude obviously it is any line that goes through the middle of both squares lol
all we need to do is find those points and then find the line that crosses them.
TODO: make sure to account for vertical lines. also think about epsilon since you'll be dealing with floats.
"""
from __future__ import annotations
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


class Square(NamedTuple):
    top_left: Point
    length: float

    def find_center(self) -> Point:
        midway_length = self.length / 2
        return Point(
            x=self.top_left.x + midway_length, y=self.top_left.y - midway_length
        )


EPSILON = 1e-6  # to avoid nasty float issues


class Line:
    @property
    def is_vertical(self):
        return self._slope is None

    @property
    def has_y_intercept(self):
        return not self.is_vertical

    @property
    def slope(self):
        if self.is_vertical:
            raise ValueError("Undefined value of vertical slope")
        return self._slope

    def __init__(self, slope, y_or_x_intercept):
        self._slope = slope
        self.y_or_x_intercept = y_or_x_intercept

    @staticmethod
    def _compute_slope(p1, p2):
        denominator = p1.x - p2.x
        if abs(denominator) < EPSILON:
            return None
        numerator = p1.y - p2.y
        return numerator / denominator

    @classmethod
    def from_points(cls, p1, p2):
        slope = cls._compute_slope(p1, p2)
        if not slope:
            y_or_x_intercept = p1.x
        else:
            y_or_x_intercept = p1.y - slope * p1.x
        return Line(slope=slope, y_or_x_intercept=y_or_x_intercept)

    def __eq__(self, other: Line):
        if sum([self.is_vertical, other.is_vertical]) == 1:
            return False
        slopes_equal = (self.is_vertical and other.is_vertical) or (
            abs(self.slope - other.slope) < EPSILON
        )
        # we've already confirmed that both of them are either both vertical or both non-vertical,
        # so it's not possible for one to be a y-intercept and the other to be x-intercept
        intercepts_equal = abs(self.y_or_x_intercept - other.y_or_x_intercept) < EPSILON
        return slopes_equal and intercepts_equal


def find_bisection_line(sq1: Square, sq2: Square):
    return Line.from_points(sq1.find_center(), sq2.find_center())
