import unittest

from hard.binode import BiNode


class Test(unittest.TestCase):
    def test(self):
        root = BiNode(
            val=7,
            left_node=BiNode(val=5, left_node=BiNode(val=2), right_node=BiNode(val=6)),
            right_node=BiNode(
                val=12, left_node=BiNode(val=10), right_node=BiNode(val=15)
            ),
        )
        head, tail = root.convert_to_linkedlist()

        self.assertEqual(2, head.val)
        self.assertEqual(15, tail.val)
        in_order_traversal = []
        curr = head
        while curr:
            in_order_traversal.append(curr.val)
            curr = curr.right_node
        self.assertListEqual([2, 5, 6, 7, 10, 12, 15], in_order_traversal)


if __name__ == "__main__":
    unittest.main()
