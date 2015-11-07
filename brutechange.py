import itertools
import math

def brute(amount, denoms):
    arr = []
    for denom in denoms:
        arr += [denom] * math.ceil(amount / denom)
    return arr

def makeChange(amount, denoms):
    denoms = sorted(denoms)
    allVals = brute(amount, denoms)
    allPossibilities = []
    for r in range(2, math.ceil(amount / denoms[0])):
        for perm in itertools.combinations(allVals, r):
            if perm in allPossibilities:
                break
            if sum(perm) == amount:
                allPossibilities.append(perm)
                break
    return allPossibilities

denoms = [3, 5, 7]
amount = 40

print(makeChange(amount, denoms))
