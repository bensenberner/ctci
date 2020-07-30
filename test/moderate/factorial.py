from unittest import TestCase

from moderate.factorial import count_trailing_zeros


class Test(TestCase):
    def test(self):
        self.assertEqual(0, count_trailing_zeros(4))
        self.assertEqual(2, count_trailing_zeros(14))
        # 4470115461512684340891257138125051110076800700282905015819080092370422104067183317016903680000000000000000
        self.assertEqual(16, count_trailing_zeros(73))
