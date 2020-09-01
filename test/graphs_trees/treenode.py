import unittest

from graphs_trees import TreeNode


class TestTreeNode(unittest.TestCase):
    def test_eq(self):
        a = TreeNode(5, left=TreeNode(6), right=TreeNode(7))
        b = TreeNode(5, left=TreeNode(6), right=TreeNode(7))
        self.assertEqual(a, b)

    def test_asymmetrical_not_equal(self):
        left = TreeNode(5, left=TreeNode(6))
        right = TreeNode(5, right=TreeNode(6))
        self.assertNotEqual(left, right)
