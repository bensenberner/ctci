def function(denoms, targetSum):
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
    print(minCoinsArr)
    return minArr

print(function([1, 3, 7], 11))


def checkListEmpty(arr):
    for i in arr:
        if i:
            return False
    return True
