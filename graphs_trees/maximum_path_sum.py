"""
# from https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, best_dual_sum, best_linear_sum):
        self.best_dual_sum = best_dual_sum
        self.best_linear_sum = best_linear_sum

def maxPathSumHelper(root, isTopLevel):
    if not root: return Node(-float('inf'), 0)
    leftRes = self.maxPathSumHelper(root.left, False)
    rightRes = self.maxPathSumHelper(root.right, False)
    best_dual_sum_from_res = max(leftRes.best_dual_sum, rightRes.best_dual_sum)
    possible_dual_sums = [
        best_dual_sum_from_res,
        leftRes.best_linear_sum + rightRes.best_linear_sum + root.val,
        root.val
    ]
    if isTopLevel:
        possible_dual_sums.extend([root.val + leftRes.best_linear_sum, root.val + rightRes.best_linear_sum])
    best_dual_sum = max(possible_dual_sums)
    best_linear_sum = max(0, leftRes.best_dual_sum, rightRes.best_dual_sum)
    return Node(best_dual_sum, best_linear_sum + root.val)

def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    res = self.maxPathSumHelper(root, True)
    return res.best_dual_sum
