def maxCans(sizes, prices, targetVal):
    cans = [0 for x in range(100)]
    minPrices = [float('inf') for x in range(100)]
    for i in range(len(cans)):
        for j in range(len(prices)):
            if i - sizes[j] < 0:
                if prices[j] < minPrices[i]:
                    minPrices[i] = prices[j]
                    cans[i] = sizes[j]
            else:
                if minPrices[i]

