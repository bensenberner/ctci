"""
A child is running up a staircase with n steps and can hop either 1, 2, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""


def num_ways_to_run_up_stairs(n):
    step_sizes = [1, 2, 3]
    num_way_to_climb_stair = [0 for _ in range(n + 1)]
    num_way_to_climb_stair[0] = 1
    for stair_idx in range(1, n + 1):
        for step_size in step_sizes:
            if stair_idx - step_size < 0:
                continue
            num_way_to_climb_stair[stair_idx] += num_way_to_climb_stair[
                stair_idx - step_size
            ]
    return num_way_to_climb_stair[n]
