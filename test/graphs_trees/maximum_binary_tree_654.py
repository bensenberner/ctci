import unittest

from graphs_trees import TreeNode
from graphs_trees.maximum_binary_tree import constructMaximumBinaryTree


class Test(unittest.TestCase):
    def test(self):
        arr = [3, 2, 1, 6, 0, 5]
        expected = TreeNode(
            val=6,
            left=TreeNode(val=3, right=TreeNode(val=2, right=TreeNode(val=1))),
            right=TreeNode(val=5, left=TreeNode(val=0)),
        )
        actual = constructMaximumBinaryTree(arr)
        self.assertEqual(expected, actual)
