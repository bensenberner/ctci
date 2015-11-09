def maxApples(arr):
    dp = [[0]*len(arr)]*len(arr[0])
    dp[0][0] = arr[0][0]
    for row in range(0, len(arr)):
        for column in range(0, len(arr[0])):
            above = dp[row - 1][column] if row > 0 else 0
            left = dp[row][column - 1] if column > 0 else 0
            dp[row][column] = arr[row][column] + max(above, left)
    return dp[row-1][column-1]

a = [[4, 2, 6, 3],
     [1, 1, 8, 4],
     [1, 1, 1, 4],
     [100, 1, 1, 7]]

print(maxApples(a))
