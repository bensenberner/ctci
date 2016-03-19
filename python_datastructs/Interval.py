class Interval(object):

    def __init__(self, s, e):
        self.start = s
        self.end = e

    def compare(self, otherInterval):
        return self if self.start < otherInterval.start else otherInterval
