def findTriplets(arr, k):
    countHash = {}
    allTriplets = set()
    for num in arr:
        if num not in countHash:
            countHash[num] = 1
        else:
            countHash[num] += 1

    # try all possible pairs
    for num1 in countHash:
        countHash[num1] -= 1
        for num2 in countHash:
            countHash[num2] -= 1
            target = k - (num1 + num2)
            if target in countHash and countHash[target] > 0:
                allTriplets.add(tuple(sorted([num1, num2, target])))
            countHash[num2] += 1
        countHash[num1] += 1
    return allTriplets

nums = [2, 5, 8, 2, 1, 8, 9, 2, 7]
k = 10
print(findTriplets(nums, k))
