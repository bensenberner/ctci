from typing import List

from hard.longest_word import TrieNode


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    m, n = len(board), len(board[0])
    root_node = TrieNode.create_from_words(words)
    results = set()
    visited_positions = set()

    def is_valid_position(i, j):
        return 0 <= i < m and 0 <= j < n

    def get_unvisited_neighbor_indexes(i, j):
        for row_delta, col_delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = i + row_delta, j + col_delta
            if (
                is_valid_position(new_i, new_j)
                and (new_i, new_j) not in visited_positions
            ):
                yield new_i, new_j

    def dfs(i, j, node):
        visited_positions.add((i, j))
        if node.is_leaf:
            results.add(node.string)
        for new_i, new_j in get_unvisited_neighbor_indexes(i, j):
            new_letter = board[new_i][new_j]
            if new_letter in node.children:
                dfs(new_i, new_j, node.children[new_letter])
        visited_positions.remove((i, j))

    for row_idx in range(m):
        for col_idx in range(n):
            letter = board[row_idx][col_idx]
            if letter in root_node.children:
                dfs(row_idx, col_idx, root_node.children[letter])

    return list(results)
