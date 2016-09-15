class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructLinkedlists(node):
    q = [(node, 0)]
    result = []

    while q:
        currNode, currDepth = q.pop()
        while len(result) - 1 < currDepth:
            result.append([])

        result[currDepth].append(currNode.val)

        if currNode.left:
            q.insert(0, (currNode.left, currDepth + 1))
        if currNode.right:
            q.insert(0, (currNode.right, currDepth + 1))
    return result

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
    for l in lists:
        print(l)
