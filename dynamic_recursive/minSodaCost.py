from copy import deepcopy
sizes = [1, 6, 12, 25, 36]
prices = [0.8, 4.0, 7.5, 14.0, 20]
def maxNumCans(sizes, prices, targetAmount):
    dp = [0]
    amount = 0
    i = 1
    while amount < targetAmount:
        minAmount = float('inf')
        for size, price in zip(sizes, prices):
            if i - size >= 0:
                minAmount = min(minAmount, dp[i - size] + price)
        dp.append(minAmount)
        i += 1
        amount = minAmount

    return i - 2 if amount > targetAmount else i - 1

def minCostCombo(sizes, prices, n):
    dp = [0] + [float('inf')] * (n - 1)
    combos = [[0 for x in range(len(prices))] for x in range(n)]

    for i in range(n):
        for j, (size, price) in enumerate(zip(sizes, prices)):
            if i - size >= 0 and dp[i - size] + price < dp[i]:
                    dp[i] = dp[i - size] + price
                    combos[i] = deepcopy(combos[i - size])
                    combos[i][j] += 1
    return combos[-1]


targetAmount = 100
targetPrice = 52.8

print("Maximum number of sodas that you can buy with " + str(targetPrice) + \
        " is " + str(maxNumCans(sizes, prices, targetPrice)))

print("Minimum cost for buying " \
        + str(targetAmount) + " cans is " + \
        str(minCostCombo(sizes, prices, targetAmount)))
