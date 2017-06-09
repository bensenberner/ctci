def cutrod(prices, n):
    bestrevs = [0 for _ in range(n+1)]
    for j in range(1, n+1):
        currMax = -float('inf')
        for i in range(1, j+1):
            currMax = max(currMax, prices[i] + bestrevs[j-i])
        bestrevs[j] = currMax
    return bestrevs[n]

if __name__ == "__main__":
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    best = cutrod(prices, 4)
    print(best)
