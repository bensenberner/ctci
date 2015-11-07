def count(denoms, m, n):
    if n == 0: return 1
    if n < 0: return 0
    if m <= 0 and n >= 1: return 0
    return count(denoms, m - 1, n) + count(denoms, m, n - denoms[m - 1])

a=[6, 9, 20]
print(count(a, len(a), 21))
