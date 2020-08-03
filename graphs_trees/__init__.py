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
        return f"L:{self.left.val if self.left else None}|self:{self.val}|R:{self.right.val if self.right else None}"
