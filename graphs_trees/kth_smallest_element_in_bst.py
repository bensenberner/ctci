from graphs_trees import TreeNode


def kthSmallest(root: TreeNode, k: int) -> int:
    count = 0
    result = -1

    def dfs(node):
        nonlocal count
        nonlocal result
        if node.left:
            dfs(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        if node.right:
            dfs(node.right)

    dfs(root)
    return result
