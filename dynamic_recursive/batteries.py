from collections import defaultdict
from copy import deepcopy
from sys import argv

'''
You want to buy N batteries. You can only buy packs of 20, 6, and 9. Can you buy the N batteries using only combinations of those packs? If so, which combinations will work?
'''

vals = [6, 9, 20]

def createPack(v):
    return tuple((1 if val == v else 0) for val in vals)

def update_tuple(t, idx, v):
    lst = list(t)
    lst[idx] += v
    return tuple(lst)

def batteries(n):
    packs = defaultdict(set)
    for i in range(1, n+1):
        for val_idx, val in enumerate(vals):
            diff = i - val
            if diff == 0:
                newpack = createPack(val)
                packs[i].add(newpack)
            elif diff in packs:
                pack_set = packs[diff]
                for pack in pack_set:
                    newpack = update_tuple(pack, val_idx, 1)
                    packs[i].add(newpack)
    return packs

def main():
    n = int(argv[1])
    packs = batteries(n)
    print(packs[n])

main()
