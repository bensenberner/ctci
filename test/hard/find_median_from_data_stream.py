import unittest

from hard.find_median_from_data_stream import MedianFinder


class Test(unittest.TestCase):
    def test_negatives(self):
        mf = MedianFinder()
        mf.addNum(-1)
        self.assertEqual(-1, mf.findMedian())
        mf.addNum(-2)
        self.assertEqual(-1.5, mf.findMedian())
        mf.addNum(-3)
        self.assertEqual(-2, mf.findMedian())
        mf.addNum(-4)
        self.assertEqual(-2.5, mf.findMedian())
        mf.addNum(-5)
        self.assertEqual(-3, mf.findMedian())

    def test(self):
        mf = MedianFinder()
        mf.addNum(1)
        self.assertEqual(1, mf.findMedian())
        mf.addNum(2)
        self.assertEqual(1.5, mf.findMedian())
        mf.addNum(3)
        self.assertEqual(2, mf.findMedian())
        mf.addNum(4)
        self.assertEqual(2.5, mf.findMedian())
        mf.addNum(5)
        self.assertEqual(3, mf.findMedian())

    def test_nothing(self):
        mf = MedianFinder()
        self.assertIsNone(mf.findMedian())

    def test_negative(self):
        mf = MedianFinder()
        mf.addNum(-45)
        self.assertEqual(-45, mf.findMedian())


if __name__ == "__main__":
    unittest.main()
