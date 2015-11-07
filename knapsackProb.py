from itertools import combinations

# So brute that its skull is 3 inches thick

def findPoss(denoms, n):
    allDenoms = []
    for denom in denoms:
        i = denom
        while i < n:
            if i not in allDenoms:
                allDenoms.append(i)
                i += i
    return final(allDenoms, n)

def final(allDenoms, n):
    if n == 0 or n in allDenoms:
        return [n]

    sols = []
    for r in range(2, len(allDenoms)):
        for subset in combinations(allDenoms, r):
            if sum(subset) == n and subset not in sols:
                sols.append(subset)
    return sols

denoms = [3, 5, 7]
n = 100
print("Denominations: " + str(denoms))
print("Target value: " + str(n))
print(findPoss(denoms, n))
