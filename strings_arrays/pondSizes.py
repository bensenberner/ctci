def isValid(i, j, m, n, land, visited):
    return i >= 0 and j >= 0 and i < m and j < n and land[i][j] == 0 and not visited[i][j]

def breadthFirstSearch(i, j, m, n, land, visited):
    currSize = 0
    if not isValid(i, j, m, n, land, visited):
        return currSize
    else:
        # include the current spot
        currSize += 1
        visited[i][j] = True
        for x in range(j-1, j+2):
            for y in range(i-1, i+2):
                currSize += breadthFirstSearch(y, x, m, n, land, visited)
        return currSize


def sizeAllPonds(land):
    sizes = []
    m = len(land)
    n = len(land[0])
    visited = [[False for j in range(n)] for i in range(m)]

    for j in range(n):
        for i in range(m):
            sizeCurrGroup = breadthFirstSearch(i, j, m, n, land, visited)
            if sizeCurrGroup > 0:
                sizes.append(sizeCurrGroup)
    return sizes


if __name__ == "__main__":
    land = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]
    print(land)
    print(sizeAllPonds(land))
