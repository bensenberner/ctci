''' Suppose you are trying to place N queens on an empty N x N chessboard.
You want to do so in such a way that no queen can be taken by any other, i.e.
no two queens occupy the same column, row, or diagonal. Print out all valid ways
of placing N queens
'''
from math import sqrt
import itertools

def printAllValid(arrangement, index, n, print_arragements=False):
    # we have reached the last position. Print the current arrangement
    if index == n:
        if print_arrangements:
            print(" ".join([str(x) for x in arrangement]))
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

        if isInLineWithThree(arrangement, index, currPos):
            return False

    return True

def isInLineWithThree(arrangement, index, currPos):
    n = len(arrangement)

    # all possible slopes of the lines
    for slopeLength in eratosthenes():
        # four possible lines from the current position
        if isInLineWithThreeUtil(arrangement, index, currPos, slopeLength, 1) or \
                isInLineWithThreeUtil(arrangement, index, currPos, -slopeLength, 1) or \
                isInLineWithThreeUtil(arrangement, index, currPos, 1, slopeLength) or \
                isInLineWithThreeUtil(arrangement, index, currPos, -1, slopeLength):
                    return True

        if slopeLength > int(sqrt(2 * (n**2))):
            break

    return False

def isInLineWithThreeUtil(arrangement, index, currPos, horizontalDelta, verticalDelta):
    numQueens = 0
    backChecker = currPos - horizontalDelta
    for i in range(index - verticalDelta, -1, -(verticalDelta)):
        if arrangement[i] == backChecker:
            numQueens += 1
            if numQueens >= 2:
                return True
        backChecker -= horizontalDelta
        if backChecker < 0 or backChecker >= len(arrangement):
            break
    return False

def eratosthenes():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {  }  # map each composite integer to its first-found prime factor
    for q in itertools.count(2):     # q gets 2, 3, 4, 5, ... ad infinitum
        p = D.pop(q, None)
        if p is None:
            # q not a key in D, so q is prime, therefore, yield it
            yield q
            # mark q squared as not-prime (with q as first-found prime factor)
            D[q*q] = q
        else:
            # let x <- smallest (N*p)+q which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = p + q
            while x in D:
                x += p
            D[x] = p

n = 11
arr = [None] * n
printAllValid(arr, 0, n)
