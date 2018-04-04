def is_valid(i, j, maze):
    m = len(maze)
    if i < 0 or i >= m: return False
    n = len(maze[i])
    return 0 <= j < n

def traverse_maze(i, j, maze, visited):
    if not is_valid(i, j, maze): return None
    if maze[i][j] == 9: return [(i, j)]
    if visited[i][j] or maze[i][j] == 5: return None
    visited[i][j] = True
    for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        result = traverse_maze(i + delta_y, j + delta_x, maze, visited)
        if result: return [(i, j)] + result

if __name__ == "__main__":
    maze = [
        [1,5,5,5,5],
        [0,5,0,0,0],
        [0,5,0,5,0,0,0,0,9],
        [0,0,0,5,0],
        [0,5,0,5,0]
    ]
    visited = [[False for element in row] for row in maze]
    found_nine = traverse_maze(0, 0, maze, visited)
    print(found_nine)
