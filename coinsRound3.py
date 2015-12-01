def main():
    c = [3, 5, 7]
    n = 43
    countNumChangeCombos(c, n)

def countNumChangeCombos(coinArr, n):
    dp = [0 for x in range(n)]

    for i in range(n):
        for coin in coinArr:
            if i == coin:
                dp[i] += 1
            if i - coin >= 0:
                if dp[i - coin] != 0:
                    dp[i] = 1 + dp[i - coin]
    print(dp)

main()
