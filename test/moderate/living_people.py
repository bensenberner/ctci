import unittest

from moderate.living_people import (
    Person,
    count_most_living_sort,
    count_most_living_bucket,
)


class MyTestCase(unittest.TestCase):
    def test_sort(self):
        people = [Person(1902, 1910), Person(1906, 1912), Person(1908, 1910)]
        self.assertEqual(3, count_most_living_sort(people))

    def test_bucket(self):
        people = [Person(1902, 1910), Person(1906, 1912), Person(1908, 1910)]
        self.assertEqual(3, count_most_living_bucket(people))
