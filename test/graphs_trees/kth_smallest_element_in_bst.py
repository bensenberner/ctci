import unittest

from graphs_trees import TreeNode
from graphs_trees.kth_smallest_element_in_bst import kthSmallest


class Test(unittest.TestCase):
    def test(self):
        root = TreeNode(
            val=3, left=TreeNode(val=1, right=TreeNode(val=2)), right=TreeNode(val=4)
        )
        self.assertEqual(4, kthSmallest(root, 4))
