class Line():
    def __init__(self, p1, p2):
        self.setSlope(p1, p2)
        self.setIntercept(p1)

    def setSlope(self, p1, p2):
        self.m = (p1[1] - p2[1]) / (p1[0] - p2[0])

    def setIntercept(self, point):
        self.b = point[1] - self.m * point[0]

    def pointLiesAboveOrOn(self, point):
        predY = self.m * point[0] + self.b
        return point[1] >= predY

def numNonDominatable(entities):
    maxX = (-float('inf'), -float('inf'))
    maxY = (-float('inf'), -float('inf'))
    for entity in entities:
        if entity[0] > maxX[0]:
            maxX = entity
        if entity[1] > maxY[1]:
            maxY = entity

    dominatingLine = Line(maxX, maxY)
    count = 0
    for entity in entities:
        if dominatingLine.pointLiesAboveOrOn(entity):
            count += 1
    return count

if __name__ == "__main__":
    entities = [
        (1, 6),
        (2, 8),
        (0, 9),
        (6, 2),
        (3, 3),
        (4, 7),
    ]
    print(numNonDominatable(entities))
