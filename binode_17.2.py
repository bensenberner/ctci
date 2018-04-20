class BiNode:
    def __init__(self, node1, node2, data):
        self.node1 = node1
        self.node2 = node2
        self.data = data

    def __repr__(self):
        return str(self.data)

def treeToList(root):
    if not root:
        return None, None
    leftHead, leftTail = treeToList(root.node1)
    rightHead, rightTail = treeToList(root.node2)
    root.node1 = leftTail
    if leftTail:
        leftTail.node2 = root
    root.node2 = rightHead
    if rightHead:
        rightHead.node1 = root
    return leftHead if leftHead else root, rightTail if rightTail else root

if __name__ == "__main__":
    a = BiNode(None, None, 20)
    b = BiNode(None, None, 35)
    c = BiNode(b, None, 40)
    d = BiNode(a, c, 30)
    head, tail = treeToList(d)
    while head:
        print(head)
        head = head.node2
    while tail:
        print(tail)
        tail = tail.node1