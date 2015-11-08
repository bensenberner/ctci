def isLarger(box1, box2):
    for d1, d2 in zip(box1, box2):
        if d1 <= d2:
            return False
    return True


def getVolume(box):
    vol = 1
    for d in box:
        vol *= d
    return vol

def findTallest(boxes, height):
    sortedBoxes = sorted(boxes, key=getVolume)

