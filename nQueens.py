''' Suppose you are trying to place N queens on an empty N x N chessboard.
You want to do so in such a way that no queen can be taken by any other, i.e.
no two queens occupy the same column, row, or diagonal. Print out all valid ways
of placing N queens
'''


def printAllValid(arrangement, index, n):
    # we have reached the last position. Print the current arrangement
    if index == n:
        print(arrangement)
        return

    for i in range(n):
        # attempt all valid placements
        if isValidPlacement(arrangement, index, i):
            arrangement[index] = i
            printAllValid(arrangement, index + 1, n)
    # after the loop is finished, we have tried all possible placements at
    # this index along the arrangements. Now, we recurse back up and try an
    # earlier index.

def isValidPlacement(arrangement, index, currPos):
    for i in range(index):
        # occupy the same column
        if currPos == arrangement[i]:
            return False

        # occupy the same diagonal, or of the same same vertical and horizontal
        # distance from one another
        if abs(currPos - arrangement[i]) == abs(index - i):
            return False

    return True

n = 8
arr = [None] * n
printAllValid(arr, 0, n)
