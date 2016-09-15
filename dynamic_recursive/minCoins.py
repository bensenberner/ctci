def minCoins(coinArr, n):
    # trying to make n cents using the coin denominations in coinArr
    table = [float('inf') for x in range(n+1)]
    table[0] = 0
    for i in range(len(table)):
        for coin in coinArr:
            if coin <= i:
                if table[i-coin] != float('inf') and table[i-coin]+1 < table[i]:
                    table[i] = table[i-coin]+1
    return table[-1]

def main():
    coins = [6, 9, 20]
    n = 7
    print(minCoins(coins, n))

main()
