def maximizeCans(sizes, costs, targetCost):
    numCans = 0
    for i in costs[::-1]:
        isZero = False
        while targetCost > costs[i]:
            if targetCost - costs[i] < 0:
                isZero = True
                break
            targetCost -= costs[i]
            numCans += sizes[i]
        if isZero:
            break

    return numCans
