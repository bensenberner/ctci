from graphs_trees import TreeNode


def in_order_traversal(node: TreeNode):
    result = []
    stack = [node]
    processed = set()
    while stack:
        curr = stack[-1]
        if curr.left and id(curr.left) not in processed:
            stack.append(curr.left)
            processed.add(id(curr.left))
            continue
        result.append(curr.val)
        stack.pop()
        if curr.right and id(curr.right) not in processed:
            stack.append(curr.right)
            processed.add(id(curr.right))
    return result
