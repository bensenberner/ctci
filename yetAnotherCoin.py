from itertools import combinations


def minChange(denoms, targetSum):
    minArr = [float("inf")] * (targetSum + 1)
    minCoinsArr = [[]] * (targetSum + 1)
    minArr[0] = 0
    for s in range(1, targetSum + 1):
        for denomDex in range(0, len(denoms)):
            currDenom = denoms[denomDex]
            if s - currDenom < 0:
                continue
            if currDenom <= s and minArr[s - currDenom] + 1 < minArr[s]:
                minArr[s] = minArr[s - currDenom] + 1
                minCoinsArr[s] = minCoinsArr[s - currDenom] + [currDenom]
                # minArr[s][1] = minArr[s - currDenom][1] + [currDenom]

    return minCoinsArr[targetSum]

if __name__ == "__main__":
    rangeOfDenoms = [1, 2, 5, 10, 20, 25, 50]
    allDenoms = [[perm for perm in combinations(rangeOfDenoms, r)] for r in range(3, 9)]
    for setOfDenoms in allDenoms:
        for total in range(1, 101):
            currTotal = minChange(setDenoms, total)

    # targetSum = int(input("Enter the sum of change you'd like to make: "))
    # print("You need these denominations: " + str(minChange(denoms, targetSum)))
