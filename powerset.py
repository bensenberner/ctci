from copy import deepcopy

def makeSets(arr):
    # if I did this in a strongly typed language then I would have
    # to make the size of sets n(n+1)/2
    sets = []
    for i in range(0, len(arr) + 1):
        if i == 0:
            sets.append[arr[i]]
            continue


    # for setSize in range(0, len(arr) + 1):
        # for i in range(0, len(arr) - setSize):
            # sets.append(arr[i:i+setSize + 1])
    return sets

if __name__ == "__main__":
    a = [2, 4, 1, 3]
    print(makeSets(a))
