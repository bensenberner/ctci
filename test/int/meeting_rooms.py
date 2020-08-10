import unittest

from int.meeting_rooms import assign_meetings_to_rooms, Meeting


class Test(unittest.TestCase):
    def test(self):
        meetings = [(0, 5), (3, 7), (6, 10), (8, 11)]
        assignments = assign_meetings_to_rooms(meetings)
        expected_assignments = {
            0: [
                Meeting(start_time=0, end_time=5, room_idx=0),
                Meeting(start_time=6, end_time=10, room_idx=0),
            ],
            1: [
                Meeting(start_time=3, end_time=7, room_idx=1),
                Meeting(start_time=8, end_time=11, room_idx=1),
            ],
        }
        self.assertEqual(expected_assignments, assignments)

    def test_non_overlapping_meetings(self):
        meetings = [(0, 5), (10, 12), (13, 15)]
        expected_assignments = {
            0: [
                Meeting(start_time=0, end_time=5, room_idx=0),
                Meeting(start_time=10, end_time=12, room_idx=0),
                Meeting(start_time=13, end_time=15, room_idx=0),
            ]
        }
        self.assertEqual(expected_assignments, assign_meetings_to_rooms(meetings))

    def test_all_overlapping_meetings(self):
        meetings = [(0, 10), (1, 11), (2, 12)]
        expected_assignments = {
            0: [Meeting(start_time=0, end_time=10, room_idx=0)],
            1: [Meeting(start_time=1, end_time=11, room_idx=1)],
            2: [Meeting(start_time=2, end_time=12, room_idx=2)],
        }
        self.assertEqual(expected_assignments, assign_meetings_to_rooms(meetings))


if __name__ == "__main__":
    unittest.main()
