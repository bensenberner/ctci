from typing import List

"""
imagine a robot sitting in the upper left corner of a grid with r rows and c columns
robot can only move in two directions: right and down, but certain cells are off limits,
the robot cannot step on them. find a path for the robot from the top left to the bottom right
------
This literally sounds like I could use DFS. Perform DFS, keep track of the path that you form. As you
traverse, keep adding on positions you've visited to the stack. If you reach a dead end then pop off your
current position from the stack. Duh..?
"""


def traverse_grid(grid: List[List]):
    r, c = len(grid), len(grid[0])

    def is_valid_position(i, j):
        return 0 <= i < r and 0 <= j < c and grid[i][j] == 1

    curr_pos = (0, 0)
    path = [curr_pos]

    def dfs(i, j):
        if (i, j) == (r - 1, c - 1):
            return True
        for new_i, new_j in [(i + 1, j), (i, j + 1)]:
            if is_valid_position(new_i, new_j):
                path.append((new_i, new_j))
                successful = dfs(new_i, new_j)
                if successful:
                    return True
                path.pop()

    dfs(0, 0)
    return path
