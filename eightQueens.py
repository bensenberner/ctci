import copy
GRID_SIZE=8

def placeQueens(row, columns, results):
    if row is GRID_SIZE:
        results.append(copy.deepcopy(columns))
    else:
        for col in range(0, GRID_SIZE):
            if checkValid(columns, row, col):
                columns[row] = col
                placeQueens(row + 1, columns, results)
    return results

def checkValid(columns, row1, column1):
    for row2 in range(0, row1):
        column2 = columns[row2]

        if column1 == column2: return False

        columnDistance = abs(column2 - column1)

        rowDistance = row1 - row2
        if columnDistance == rowDistance: return False

    return True

row = 0
columns = [0] * GRID_SIZE
results = []
print(len(placeQueens(row, columns, results)))
