class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append((x, min(x, self.getMin())))


    def pop(self):
        """
        :rtype: void
        """
        self.s.pop(-1)


    def _top(self):
        return self.s[-1]

    def top(self):
        """
        :rtype: int
        """
        return self._top()[0]


    def getMin(self):
        """
        :rtype: int
        """
        return self._top()[1]
