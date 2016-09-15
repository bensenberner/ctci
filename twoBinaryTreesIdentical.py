class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def isSubtreeOf(self, tree):
        queue = [tree]
        while queue:
            curr = queue.pop(0)
            print(curr)
            if areTreesIdentical(self, curr):
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False

def areTreesIdentical(t1, t2):
    if t1 is None and t2 is None:
        return True
    if (t1 is None and t2 is not None) or (t1 is not None and t2 is None):
        return False
    if t1.val != t2.val:
        return False

    return areTreesIdentical(t1.left, t2.left) and \
            areTreesIdentical(t1.right, t2.right)

if __name__ == "__main__":
    o = Node(93)
    p = Node(52)

    a = Node(1)
    b = Node(3)
    c = Node(5)
    d = Node(8)

    q = Node(1)
    w = Node(3)
    e = Node(5)
    r = Node(8)

    o.left = p
    o.right = a
    a.left = b
    a.right = c
    b.right = d

    q.left = w
    q.right = e
    w.right = r
    print(areTreesIdentical(a, q))
    print(a.isSubtreeOf(o))
