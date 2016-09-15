from itertools import combinations

rangeOfDenoms = [1, 2, 5, 10, 15, 20, 25, 50]
x = [[perm for perm in combinations(rangeOfDenoms, r)] for r in range(3, 9)]
print(x)
# for r in range(3, 9):
    # for perm in combinations(rangeOfDenoms, r):
        # print(perm)
