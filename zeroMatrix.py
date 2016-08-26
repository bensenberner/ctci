'''
Write an algorithm such that if an element in an m by n matrix is 0, its entire row and column are set to 0
'''
def zeroMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zeroOutTop = False
    for j in range(n):
        if matrix[0][j] == 0:
            zeroOutTop = True
            break

    zeroOutLeft = False
    for i in range(m):
        if matrix[i][0] == 0:
            zeroOutLeft = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # zero out the rows that were marked for deletion
    for i in range(m):
        if matrix[i][0] == 0:
            for j in range(n):
                matrix[i][j] = 0

    # zero out columns that were marked for deletion
    for j in range(n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0

    if zeroOutTop:
        for j in range(n):
            matrix[0][j] = 0

    if zeroOutLeft:
        for i in range(m):
            matrix[i][0] = 0
