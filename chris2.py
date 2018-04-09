from collections import defaultdict

def maxPoints(li):
    total = 0
    d = defaultdict(int)
    maxPointsPossible = float('-inf')
    for val in li:
        total += val
        d[val] += 1

    for val in d:
        valBelow = (val - 1) * d[val-1] if val - 1 in d else 0
        valAbove = (val + 1) * d[val+1] if val + 1 in d else 0
        maxPointsPossible = max(maxPointsPossible, total - valBelow - valAbove)
    return maxPointsPossible

print(maxPoints([1, 2, 2, 2, 3, 5]))
