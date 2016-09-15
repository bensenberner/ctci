from linkedListTreeDepths import constructLinkedlists

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getPermutations(string):
    if len(string) == 1:
        yield string
    else:
        for i in range(len(string)):
            for perm in getPermutations(string[:i] + string[i+1:]):
                yield [string[i]] + perm

def generateAllPossibleArrays(lists, possibleLists, currList, idx):
    if idx == len(lists):
        possibleLists.append(currList)
        return
    for perm in getPermutations(lists[idx]):
        generateAllPossibleArrays(lists, possibleLists, currList + perm, idx+1)

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    # a is at level 0
    # b is at level 1
    # c is at level 1
    # d is at level 2
    # e is at level 3
    # f is at level 3
    a.left = b
    a.right = c
    c.left = d
    d.right = e
    d.left = f

    lists = constructLinkedlists(a)
    possibleLists = []
    currList = []
    generateAllPossibleArrays(lists, possibleLists, currList, 0)
    i = 0
    for l in possibleLists:
        if i > 100:
            break
        print(l)
        i += 1
