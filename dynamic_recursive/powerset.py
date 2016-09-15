from copy import deepcopy

def makeSets(arr):
    arr = sorted(arr)
    # will contain all subsets. eventually grows to size 2^n
    sets = [[]]
    for num in arr:
        # lock the length before we start growing sets
        subsetLen = len(sets)
        for i in range(subsetLen):
            newSet = sets[i] + [num]

            # since it's a sorted list, we can check for duplicate lists
            sets.append(newSet) if newSet not in sets else None

    return sets

def findSubsetSums(arr, target):
    powerset = makeSets(arr)
    return [subset for subset in powerset if sum(subset) == target]

if __name__ == "__main__":
    a = [-1, 2, 3, 4, 6, -3, 6, -8]
    print(findSubsetSums(a, 5))
