def maxProfit(rodPrices, rodLen):
    dp = [-1 for x in range(rodLen+1)]
    dp[0] = 0

    for i in range(1, rodLen + 1):
        maximum = -1
        for j in range(i):
            maximum = max(maximum, rodPrices[j] + dp[i - (j+1)])
        dp[i] = maximum
    return dp[rodLen]

def main():
    rodPrices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 10
    print(maxProfit(rodPrices, n))

main()
