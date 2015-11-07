def makeSets(arr):
    sets = []
    for setSize in range(0, len(arr) + 1):
        for i in range(0, len(arr) - setSize):
            sets.append(arr[i:i+setSize + 1])
    return sets

if __name__ == "__main__":
    a = [2, 3, 4, 1]
    print(makeSets(a))
