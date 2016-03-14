def numMovesFunc(arr, idx, n, numMoves, useMoves):
    if idx == n - 1:
        return (numMoves, useMoves)

    else:
        minMoves = float('inf')
        bestMove = idx
        bestMoveUses = useMoves
        for i in range(idx+1, idx+arr[idx]):
            if i > n - 1:
                break
            (nmoves, uses) = numMovesFunc(arr, i, n, numMoves+1, useMoves + [i])
            if nmoves < minMoves:
                minMoves = nmoves
                bestMove = i
                bestMoveUses = uses

        return (minMoves, bestMoveUses)

arr = [2, 4, 1, 2, 4, 1, 2, 3, 1, 3, 2, 4, 2, 5, 2, 1, 8, 2, 3, 5, 1, 2, 3, 2, 3, 1, 4, 1]
n = len(arr)
idx = 0
numMoves = 0
useMoves = [0]
print(numMovesFunc(arr, idx, n, numMoves, useMoves))
