"""
Given any node in a BST, get the in-order successor to that node.
--------------------
     5
    / \
   3   7
  /\   /\
 2 4  6  8

5 -> 6
6 -> 7
8 -> None
"""
from __future__ import annotations

from graphs_trees import TreeNode


def find_in_order_successor(root: TreeNode, val: int):
    next_largest_parent_val = None
    curr = root
    while curr.val != val:
        if curr.val > val:
            next_largest_parent_val = curr.val
            curr = curr.left
        else:
            curr = curr.right
    if curr.right is None:
        return next_largest_parent_val
    else:  # find the smallest element of the right subtree
        curr = curr.right
        while curr.left:
            curr = curr.left
        return curr.val
