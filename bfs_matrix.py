import random
from collections import deque

def generateNeighborCoords(coord):
    i, j = coord
    return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

def bfs(matrix, i, j, n):
    queue = deque([(i, j)])
    visited = set()
    while len(queue) > 0:
        coord = queue.popleft()
        visited.add(coord)
        print(coord)
        neighborCoords = generateNeighborCoords(coord)
        for neighborCoord in neighborCoords:
            if isValid(neighborCoord, visited, n):
                queue.append(neighborCoord)

def isValid(coord, visited, n):
    x, y = coord
    return True if x >= 0 and y >= 0 and x < n and y < n and coord not in
visited else False

if __name__ == "__main__":
    random.seed()
    n = 10
    matrix = [[random.randint(10, 40) for x in range(n)] for y in range(n)]

