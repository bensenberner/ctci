"""
Given a list of people with their birth and death years, implement a method to compute the year with the msot people alive.
Assume all people were born between 1900 and 2000 (inclusive).
If a person was born during any portion of that year, they should be included in that year's count. For example
Person(birth=1908, death=1909) is included in both 1908 and 1909
------------------------------
Approach 1:
Create two lists: of just births and deaths, both sorted.
Iterate through them merge-sorted-lists-style, incrementing a counter whenever you encounter a birth,
decrementing when you see a death. Keep track of the max.
Time: O(nlog(n)) to sort the lists
Space: O(n) to store these new sorted lists

Approach 2:
Key phrase is "born between 1900 and 2000 (inclusive).
I could create an array of size 1001. Each one would contain a counter of the number of births and deaths
recorded on each year.
1. Iterate through all the people, incrementing the appropriate counters
2. Iterate through the array, in order, incrementing based on births before decrementing based on deaths.

Time: O(n) to go through all the people
Space: O(101) to store all the years
"""
from collections import deque, Counter
from enum import Enum, auto
from typing import NamedTuple, List


class Person(NamedTuple):
    birth: int
    death: int


def count_most_living_sort(people):
    # using deques for intuitive ordering of dates
    births = deque(sorted(person.birth for person in people))
    deaths = deque(sorted(person.death for person in people))
    curr_count = 0
    max_count = 0
    while births:  # births will run out before deaths
        if births[0] <= deaths[0]:
            curr_count += 1
            max_count = max(max_count, curr_count)
            births.popleft()
        else:
            curr_count -= 1
            deaths.popleft()
    return max_count


class Event(Enum):
    BIRTH = auto()
    DEATH = auto()


def count_most_living_bucket(people: List[Person]):
    life_counters = [Counter() for _ in range(101)]

    def get_idx_from_year(year):
        return year - 1900

    for person in people:
        birth_idx = get_idx_from_year(person.birth)
        life_counters[birth_idx][Event.BIRTH] += 1

        death_idx = get_idx_from_year(person.death)
        life_counters[death_idx][Event.DEATH] += 1

    curr_count = max_count = 0
    for counter in life_counters:
        curr_count += counter[Event.BIRTH]
        max_count = max(max_count, curr_count)
        curr_count -= counter[Event.DEATH]
    return max_count
