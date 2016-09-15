class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def countPaths(tree, originalNum, num):
    count = 0
    if tree.val == num:
        count += 1
    if tree.left:
        #count += countPaths(tree.left, originalNum, originalNum - tree.val)
        count += countPaths(tree.left, originalNum, num - tree.val)
    if tree.right:
        #count += countPaths(tree.right, originalNum, originalNum - tree.val)
        count += countPaths(tree.right, originalNum, num - tree.val)
    return count

if __name__ == "__main__":
    o = Node(93)
    p = Node(52)

    a = Node(2)
    b = Node(4)
    c = Node(-4)
    d = Node(-8)

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
    print(countPaths(a, 8, -2))
