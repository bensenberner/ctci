def isIncreasingSeq(seq):
    n = len(seq)
    if n <= 1: return True
    for i in range(1, n):
        if seq[i-1] >= seq[i]:
            return False
    return True

def almostIncreasingSequence(seq):
    n = len(seq)
    if isIncreasingSeq(seq):
        return True
    for i in range(n-1):
        newArr = seq[:i] + seq[i+1:]
        if isIncreasingSeq(newArr):
            return True
    return False

s = [123, -17, -5, 1, 2, 3, 12, 43, 45]
print(almostIncreasingSequence(s))
