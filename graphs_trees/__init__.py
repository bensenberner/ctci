from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(
        self, val, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<L:{self.left.val if self.left else None}|self:{self.val}|R:{self.right.val if self.right else None}>"

    def __eq__(self, other):
        self_vals = []
        other_vals = []

        def construct_flat_arr(curr_node, vals):
            if curr_node.left:
                construct_flat_arr(curr_node.left, vals)
            vals.extend([None, curr_node.val])
            if curr_node.right:
                construct_flat_arr(curr_node.right, vals)
            vals.append(None)

        construct_flat_arr(self, self_vals)
        construct_flat_arr(other, other_vals)
        return self_vals == other_vals
