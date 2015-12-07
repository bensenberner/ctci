from copy import deepcopy

def makeSets(arr):
    # if I did this in a strongly typed language then I would have
    # to make the size of sets n(n+1)/2
    sets = [[]]
    for x in arr:
        for subset in sets:
            newSet = deepcopy(subset)
            print(subset)
            newSet.append(x)
            sets = newSet + sets
            # newSet = subset + [x]
            # sets += [newSet]

    return sets

if __name__ == "__main__":
    a = [2, 4, 1, 3]
    print(makeSets(a))
