"""
Given two lines, each defined by a pair of points, determine their point of intersection, if any.

Main considerations are around:
- Vertical lines
- Parallel lines
- Vertical parallel lines
- Epsilons

we're dealing with floats here, so we gotta be careful about epsilons.

Given a pair of points $(x_1, y_1), (x_2, y_2)$
the slope is
$frac_{y_1-y_2}{x_1-x_2}$
the first issue comes when $|x_1-x_2| < epsilon$, because that means the slope
is infinite. In this case, we're going to need to set some sort of boolean,
is_vertical=True. Or we could just say `slope=None`, and then make some sort of
convenience method which checks if that is true, call it `is_vertical()`.
If the line is vertical then there is no y-intercept, unless the line is literally the y-axis,
in which case it intersects infinitely many times. But that doesn't matter: if the line is vertical then
all we care about is the x_intercept.
So rather than simply calling it `b`, we will call it `y_or_x_intercept`, and it will be clear to any
logical thinker that the true nature of that variable will be based on the value of `is_vertical`
if you have two equations:
$y = m_1 * x + b_1$
$y = m_2 * x + b_2$
the way you would find the point of intersection is to first set
$m_1 * x + b_1 = m_2 * x + b_2$
and solve for x
then plug either one of them back in to find `y`
"""
from __future__ import annotations

from typing import NamedTuple, Optional

import numpy as np


class Point(NamedTuple):
    x: float
    y: float


class Line(object):
    epsilon = 1e-9

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self._slope_or_none = self._compute_slope()
        self.y_or_x_intercept = self._compute_intercept()

    def _compute_slope(self) -> Optional[float]:
        denominator = self.p2.x - self.p1.x
        if abs(denominator) < self.epsilon:
            return None
        numerator = self.p2.y - self.p1.y
        return numerator / denominator

    def _compute_intercept(self):
        if self.is_vertical():
            return self.p1.x
        return self.p1.y - self.slope * self.p1.x

    def is_vertical(self):
        return self._slope_or_none is None

    def is_horizontal(self):
        # TODO: use this somewhere?
        return not self.is_vertical() and abs(self.slope) < self.epsilon

    @property
    def slope(self):
        if self.is_vertical():
            raise ValueError("Cannot access slope of vertical line")
        return self._slope_or_none

    def get_intersection_with(self, other: Line) -> Optional[Point]:
        # TODO: I feel like this code is a little messy. could we clean it up?
        # if the lines are parallel, return None (this includes if they are the same line). TODO: another case for this?
        # Otherwise, return the point of intersection.
        both_vertical = self.is_vertical() and other.is_vertical()
        neither_vertical = not self.is_vertical() and not other.is_vertical()
        if neither_vertical:
            are_parallel = abs(self.slope - other.slope) < self.epsilon
        else:
            are_parallel = False
        if both_vertical or are_parallel:
            return None
        if other.is_vertical() and not self.is_vertical():
            # to avoid swapping things around
            return other.get_intersection_with(self)
        if self.is_vertical():
            intersecting_y = (
                (other.p1.y - other.y_or_x_intercept) / other.slope
                if not other.is_horizontal()
                else other.y_or_x_intercept
            )
            return Point(self.p1.x, intersecting_y)
        # set up both equations as y - mx = b, then it's a system of linear equations where we solve for x and y
        a = np.array([[1, -self.slope], [1, -other.slope]])
        b = np.array([self.y_or_x_intercept, other.y_or_x_intercept])
        point_as_arr = np.linalg.solve(a, b)
        return Point(*point_as_arr)

