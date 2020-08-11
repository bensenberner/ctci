"""
Given a collection of n meetings (each one characterized by a start and end time)
Create an assignment of meetings to meeting rooms that minimizes the most number of meeting rooms
needed at any one time.
e.g.
meetings = [
  (0, 5)
  (3, 7),
  (6, 10),
  (8, 11)
]

room_to_meetings = {
  0: [(0, 5), (6, 10)]
  1: [(3, 7), (8, 11)]
}

each key in room_to_meetings represents the idx of a room. note that these could have been flipped and it wouldn't matter
---------------------
Approach 1 (unoptimized)
we know at minimum we would only need 1 meeting room (if none of the meetings overlapped)
at maximum we would need n meeting rooms (if all of them overlapped at the same time)

so, create a list to represent all the meeting rooms, and whether they were occupied
initialize them to None
meetings = [
  (0, 5)
  (3, 7),
  (6, 10),
  (8, 11)
]
rooms = [None, None, None, None]
sort the meetings by start_time
iterate through them
for each meeting:
    go through each room, starting at the beginning. If it's currently unoccupied, then occupy it. append to the appropriate
    list in room_to_meetings. Otherwise, if the meeting room is currently free (because the sorted meeting begins after the current meeting ends)
    then place the sorted meeting in this room and throw away the other meeting
Runtime: O(nlogn + n^2)
Space: O(n)
we can do better. We don't need to iterate through all the meetings.

Approach 2: Optimized (TODO)
Created a min heap in which the key of the heap represents the end time of a meeting
"""
from __future__ import annotations

import heapq
import operator
from collections import defaultdict
from typing import List, Tuple, NamedTuple


class Meeting(NamedTuple):
    end_time: int
    start_time: int
    room_idx: int


def assign_meetings_to_rooms(meetings: List[Tuple[int, int]]):
    minheap: List[Meeting] = []
    # represents the maximum index of any room that is currently occupied
    max_room_idx = 0
    assignments = defaultdict(lambda: list())
    for curr_start_time, curr_end_time in sorted(meetings, key=operator.itemgetter(0)):
        earliest_end_meeting = minheap[0] if minheap else None
        if not earliest_end_meeting or earliest_end_meeting.end_time > curr_start_time:
            new_meeting_room_idx = max_room_idx
            max_room_idx += 1
        else:
            heapq.heappop(minheap)
            new_meeting_room_idx = earliest_end_meeting.room_idx
        new_meeting = Meeting(
            end_time=curr_end_time,
            start_time=curr_start_time,
            room_idx=new_meeting_room_idx,
        )
        heapq.heappush(minheap, new_meeting)
        assignments[new_meeting_room_idx].append(new_meeting)
    return assignments
