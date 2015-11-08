mat = [[1, 2, 9],
       [12, 3, 8],
       [4, 6, 7],
       [11, 5, 10]]

longestPathLength = 0
longestPath = []

def findLongestPath(row, column, pathLength, currentPath):
    global longestPathLength
    global longestPath
    if pathLength > longestPathLength:
        longestPathLength = pathLength
        longestPath = currentPath

    currentPoint = [row, column]
    if not row < 0:
        if mat[row - 1][column] == mat[row][column] + 1:
            currentPath.append(currentPoint)
            findLongestPath(row - 1, column, pathLength + 1, currentPath)
    if not row >= len(mat) - 1:
        if mat[row + 1][column] == mat[row][column] + 1:
            currentPath.append(currentPoint)
            findLongestPath(row + 1, column, pathLength + 1, currentPath)
    if not column < 0:
        if mat[row][column - 1] == mat[row][column] + 1:
            currentPath.append(currentPoint)
            findLongestPath(row, column - 1, pathLength + 1, currentPath)
    if not column >= len(mat[0]) - 1:
        if mat[row][column + 1] == mat[row][column] + 1:
            currentPath.append(currentPoint)
            findLongestPath(row, column + 1, pathLength + 1, currentPath)

def main():
    for r in range(0, len(mat)):
        for c in range (0, len(mat[0])):
            findLongestPath(r, c, 0, [])

main()
print(longestPathLength)
print(longestPath)
