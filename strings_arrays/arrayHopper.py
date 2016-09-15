def arrHopper(arr, n):
    dp = [0 for x in range(n)]
    dp[n-1] = 0

    # build the list of best possible moves
    for i in range(n-2, -1, -1):
        minMoves = float('inf')
        for j in range(i+1, i+arr[i]+1):
            if j > n - 1:
                continue
            minMoves = min(minMoves, dp[j])
        dp[i] = minMoves + 1

    moves = [0]
    curr = 0

    while curr < n:
        minPos = curr+1
        minHops = float('inf')
        for pos in range(curr+1, curr+arr[curr]+1):
            if dp[pos] == 0:
                moves.append(pos)
                return moves
            else:
                if dp[pos] < minHops:
                    minHops = dp[pos]
                    minPos = pos

        curr = minPos
        moves.append(minPos)

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9, 3, 5, 3, 4, 3, 1, 3, 4, 2, 3, 4, 2, 3, 3]
print(arr)
print(arrHopper(arr, len(arr)))
