'''
Given two line segments, find the point of intersection, if one exists.
A point is represented as an n-dimensional vector. If no point of intersection
exists, then return None.

Question: what if the points are n-dimensional?
    deal w it
Question: what to do if the dimensionality of the points are different? (dw
about it)
Question: what if the lines line up? There could be overlap, but not complete
overlap. (that's a special case, you can figure that out)
'''
class Point():
    def __init__(self, dims):
        self.dims = dims

class LineSeg():
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

def findPointOfIntersection(line1, line2):

if __name__ == "__main__":
    p1 = [1, 2, 3]
    p2 = [3, 4, 5]
    p3 = [4, 5, 6]
    p4 = [5, 6, 7]
