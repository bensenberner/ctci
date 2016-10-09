def allPossibleLengthsNaive(small, large, currNumPieces, currLen, k, lengths):
    if currNumPieces == k:
        lengths.add(currLen)
        return
    currNumPieces += 1
    for piece in [small, large]:
        allPossibleLengthsNaive(small, large, currNumPieces, currLen + piece, k, lengths)

def allPossibleLengths(small, large, k):
    diff = large - small
    if large == small:
        return [diff]
    currLen = small * k
    # if you wanted to, you could preallocate the space for this array, but
    # whatever
    lengths = [currLen]
    for i in range(k):
        currLen += diff
        lengths.append(currLen)

    return lengths

if __name__ == "__main__":
    small = 3
    large = 5
    k = 5
    lengths = set()
    allPossibleLengthsNaive(small, large, 0, 0, k, lengths)
    print(lengths)
    print(allPossibleLengths(small, large, k))
