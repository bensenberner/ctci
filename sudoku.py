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
    grid = [[None, None, None, None, None, None, None, None, 7],
            [5, None, 1, None, 3, None, 4, None, 8],
            [None, 9, 4, None, 1, None, 3, None, None],
            [None, None, 7, None, None, 3, None, None, None],
            [None, 2, 8, 9, None, 5, 7, 3, None],
            [None, None, None, 1, None, None, 6, None, None],
            [None, None, 5, None, 2, None, 8, 7, None],
            [9, None, 2, None, 6, None, 5, None, 4],
            [7, None, None, None, None, None, None, None, None]]

    for row in grid:
        print(row)
    print('\n')
    if solve(grid):
        for row in grid:
            print(row)
    else:
        print("No sol")

main()
