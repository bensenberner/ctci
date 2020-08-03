from unittest import TestCase

from graphs_trees import TreeNode
from graphs_trees.next_largest_successor import find_in_order_successor


def create_root():
    return TreeNode(
        val=5,
        left=TreeNode(val=3, left=TreeNode(val=2), right=TreeNode(val=4)),
        right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=8)),
    )


class Test(TestCase):
    def test_root(self):
        self.assertEqual(6, find_in_order_successor(create_root(), 5))

    def test_no_successor(self):
        self.assertEqual(None, find_in_order_successor(create_root(), 8))

    def test_parent_successor(self):
        self.assertEqual(3, find_in_order_successor(create_root(), 2))

    def test_5(self):
        self.assertEqual(6, find_in_order_successor(create_root(), 5))
