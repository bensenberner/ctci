MAX_NUM = 9

def solve(grid):
    # no more places to find
    i, j = findUnassignedLocation(grid)
    if i is None:
        return True
    # try every number
    for possNum in range(1, MAX_NUM + 1):
        if isValid(grid, i, j, possNum):
            grid[i][j] = possNum
            if solve(grid):
                return True
            grid[i][j] = None
    return False

def findUnassignedLocation(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == None:
                return (i, j)
    return (None, None)

def isValid(grid, i, j, n):
    return isValidRow(grid, i, n) \
            and isValidColumn(grid, j, n) \
            and isValidSquare(grid, i - i%3, j - j%3, n)

def isValidRow(grid, row, num):
    for i in range(len(grid[0])):
        if grid[row][i] == num:
            return False
    return True

def isValidColumn(grid, column, num):
    for i in range(len(grid)):
        if grid[i][column] == num:
            return False
    return True

def isValidSquare(grid, rowStart, columnStart, num):
    for i in range(3):
        for j in range(3):
            if grid[rowStart + i][columnStart + j] == num:
                return False
    return True

def main():
    grid = [[3, None, 6, 5, None, 8, 4, None, None],
            [5, 2, None, None, None, None, None, None, None],
            [None, 8, 7, None, None, None, None, 3, 1],
            [None, None, 3, None, 1, None, None, 8, None],
            [9, None, None, 8, 6, 3, None, None, 5],
            [None, 5, None, None, 9, None, 6, None, None],
            [1, 3, None, None, None, None, 2, 5, None],
            [None, None, None, None, None, None, None, 7, 4],
            [None, None, 5, 2, None, 6, 3, None, None]]
    if solve(grid):
        for row in grid:
            print(row)
    else:
        print("No sol")

main()
