'''
creates a list of squares from 1, 4, 9 ... up until num
'''
def getSquares(num):
    currNum = 1
    res = []
    while currNum ** 2 <= num:
        res.append(currNum ** 2)
        currNum += 1
    return res

def findMinNumSquares(num, dp, squares):
    if num < 0:
        return 0
    if dp[num]:
        return dp[num]
    # find the largest square that could have been used in constructing this
    # number (still has to be less than the number itself)
    i = len(squares) - 1
    while squares[i] > num:
        i -= 1
    minSoFar = float('inf')
    # try all the possible squares that could have been used to sum this number
    for j in range(i, -1, -1):
        curr = findMinNumSquares(num - squares[j], dp, squares) + 1
        minSoFar = min(curr, minSoFar)
    # remember the min for this number to potentially save time
    dp[num] = minSoFar
    return minSoFar

if __name__ == "__main__":
    num = 24
    squares = getSquares(num)
    dp = [None for x in range(num+1)]
    dp[0] = 0
    # every square only takes one square to sum to itself (trivially)
    for square in squares:
        dp[square] = 1
    print(findMinNumSquares(num, dp, squares))
