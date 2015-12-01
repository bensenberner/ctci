def allCoinChange(coinArr, n):
    dp = [  [ [] ] for x in range(n)]
    for i in range(len(dp)):
        for coin in coinArr:
            if i - coin == 0:
                dp[i].append([coin])
            # if the i - coin index is not empty, add everything in it
            # to the current thing
            elif dp[i - coin] != [[]]:
                if len(dp[i-coin]) == 1:
                    dp[i].append([coin, dp[i-coin]])
                else:
                    for prevArr in dp[i - coin]:
                        dp[i].append([coin] + prevArr)
    return dp[-1]

def main():
    coinArr = [3, 7, 20]
    n = 31
    print(allCoinChange(coinArr, n))

main()
