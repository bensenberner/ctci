from unittest import TestCase

from moderate.make_change import min_num_coins_to_make_change_for


class Test(TestCase):
    def test(self):
        self.assertEqual(4, min_num_coins_to_make_change_for(31))
