from __future__ import annotations

from typing import Optional, Tuple


class BiNode:
    def __init__(
        self,
        val,
        left_node: Optional[BiNode] = None,
        right_node: Optional[BiNode] = None,
    ):
        self.val = val
        self.left_node = left_node
        self.right_node = right_node

    def convert_to_linkedlist(self) -> Tuple[BiNode, BiNode]:
        left_head, left_tail, right_head, right_tail = self, self, self, self
        if not (self.left_node or self.right_node):
            return left_head, right_tail
        if self.left_node:
            left_head, left_tail = self.left_node.convert_to_linkedlist()
            self.left_node = left_tail
            left_tail.right_node = self
        if self.right_node:
            right_head, right_tail = self.right_node.convert_to_linkedlist()
            self.right_node = right_head
            right_head.left_node = self
        return left_head, right_tail
