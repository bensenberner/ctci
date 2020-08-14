from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    memo = [[None for _ in range(n)] for __ in range(m)]

    def is_valid_position(row_idx, col_idx):
        return 0 <= row_idx < m and 0 <= col_idx < n

    def valid_adjacent_indexes(row_idx, col_idx):
        for row_diff, col_diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_row_idx = row_idx + row_diff
            new_col_idx = col_idx + col_diff
            if (
                is_valid_position(new_row_idx, new_col_idx)
                and matrix[new_row_idx][new_col_idx] > matrix[row_idx][col_idx]
            ):
                yield new_row_idx, new_col_idx

    def dfs(row_idx, col_idx):
        if memo[row_idx][col_idx] is not None:
            return memo[row_idx][col_idx]
        path_len = 0
        for new_row_idx, new_col_idx in valid_adjacent_indexes(row_idx, col_idx):
            path_len = max(path_len, 1 + dfs(new_row_idx, new_col_idx))
        memo[row_idx][col_idx] = path_len
        return path_len

    max_val = 0
    for i in range(m):
        for j in range(n):
            max_val = max(max_val, dfs(i, j))
    return max_val + 1
