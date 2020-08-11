import unittest

from dynamic_recursive.triple_step import num_ways_to_run_up_stairs


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(1, num_ways_to_run_up_stairs(1))
        self.assertEqual(2, num_ways_to_run_up_stairs(2))
        self.assertEqual(4, num_ways_to_run_up_stairs(3))
        self.assertEqual(7, num_ways_to_run_up_stairs(4))


if __name__ == "__main__":
    unittest.main()
