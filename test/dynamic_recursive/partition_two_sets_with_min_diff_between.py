import unittest

from dynamic_recursive.partition_two_sets_with_min_diff_between import min_partition


class Test(unittest.TestCase):
    def assertAbsoluteDiffInPartitionSum(self, expected_diff, left, right):
        self.assertEqual(expected_diff, abs(sum(left) - sum(right)))

    def test1(self):
        arr = [1, 6, 12, 5]
        left, right = min_partition(arr)
        self.assertAbsoluteDiffInPartitionSum(0, left, right)

    def test2(self):
        arr = [5, 8, 2, -6]
        left, right = min_partition(arr)
        self.assertAbsoluteDiffInPartitionSum(1, left, right)
