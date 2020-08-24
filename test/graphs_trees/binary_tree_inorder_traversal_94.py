import unittest

from graphs_trees import TreeNode
from graphs_trees.binary_tree_inorder_traversal_94 import in_order_traversal


class MyTestCase(unittest.TestCase):
    def test_lc(self):
        root = TreeNode(
            val=1, left=None, right=TreeNode(2, left=TreeNode(val=3), right=None)
        )
        self.assertEqual([1, 3, 2], in_order_traversal(root))
