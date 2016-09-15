def naiveSubsetSum(arr, target):
    arr.sort()
    oldSubsets = []
    for element in arr:
        newSubsets = []
        newSubsets += [element] if element <= target else None
        for old in oldSubsets:
            currentSubset = old + [element]
            currSum = curr
