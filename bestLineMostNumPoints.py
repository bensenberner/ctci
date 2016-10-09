def findSlope(p1, p2):
    return (p2[1] - p1[1])/(p2[0] - p1[0])

def findIntercept(p, slope):
    return p[1] - slope * p[0]

def findBestLine(points):
    lines = {}
    n = len(points)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            slope = findSlope(points[i], points[j])
            intercept = findIntercept(points[i], slope)
            slope_intercept_tuple = (slope, intercept)
            if slope_intercept_tuple not in lines:
                lines[(slope_intercept_tuple)] = set([points[i], points[j]])
            else:
                lines[(slope_intercept_tuple)].add(points[i])
                lines[(slope_intercept_tuple)].add(points[j])

    maxPoints = set()
    maxLine = None
    for line in lines:
        if len(lines[line]) > len(maxPoints):
            maxPoints = lines[line]
            maxLine = line
    return maxLine, maxPoints

if __name__ == "__main__":
    points = [(1, 1), (2, 2), (3, 3), (4, 1), (1, 4), (5, 2)]
    print(points)
    print(findBestLine(points))
