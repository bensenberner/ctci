def countWays(amount, coins):
    coins = sorted(coins)
    dp = [1] + [0] * amount

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    print(dp)
    return dp[amount]

print(countWays(4, [1, 2, 3]))
