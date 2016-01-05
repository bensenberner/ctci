from python_datastructs import Trie

def main():
    # build the trie
    with open('/usr/share/dict/words', 'r') as f:
        # the [:-1] omits the newline chars
        wordSet = set([word.lower()[:-1] for word in f.readlines()[:]])
        trie = Trie.Trie()
        trie.insertList(wordSet)

    letterGrid = "raneudo,"+\
                 "alodrat,"+\
                 "terilwe,"+\
                 "amopuam,"+\
                 "lemimye,"+\
                 "seopnas,"+\
                 "mesicae"

    grid = convertGrid(letterGrid)
    foundWords = set()

    solveBoggle(grid, trie, foundWords)

    longestWords = sorted(list(foundWords), reverse=True, key=len)

    # print results
    for line in grid:
        print(line)
    print(longestWords)

def convertGrid(letters):
    return [list(s) for s in letters.split(',')]

def solveBoggle(grid, trie, foundWords):
    visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if trie.validPrefix(grid[i][j]):
                exploreWord(i, j, grid, visited, trie, grid[i][j], foundWords)

def exploreWord(i, j, grid, visited, trie, currWord, foundWords):
    m = len(grid)
    n = len(grid[0])

    if trie.contains(currWord):
        foundWords.add(currWord)

    visited[i][j] = True

    # explore top left corner
    if i > 0 and j > 0 and not visited[i-1][j-1]:
        newWord = currWord + grid[i-1][j-1]
        if trie.validPrefix(newWord):
            exploreWord(i-1, j-1, grid, visited, trie, newWord, foundWords)

    # explore top right corner
    if i > 0 and j < n-1 and not visited[i-1][j+1]:
        newWord = currWord + grid[i-1][j+1]
        if trie.validPrefix(newWord):
            exploreWord(i-1, j+1, grid, visited, trie, newWord, foundWords)

    # explore bottom left corner
    if i < m-1 and j > 0 and not visited[i+1][j-1]:
        newWord = currWord + grid[i+1][j-1]
        if trie.validPrefix(newWord):
            exploreWord(i+1, j-1, grid, visited, trie, newWord, foundWords)

    # explore bottom right corner
    if i < m-1 and j < n-1 and not visited[i+1][j+1]:
        newWord = currWord + grid[i+1][j+1]
        if trie.validPrefix(newWord):
            exploreWord(i+1, j+1, grid, visited, trie, newWord, foundWords)

    # explore above
    if i > 0 and not visited[i-1][j]:
        newWord = currWord + grid[i-1][j]
        if trie.validPrefix(newWord):
            exploreWord(i-1, j, grid, visited, trie, newWord, foundWords)

    # explore below
    if i < m-1 and not visited[i+1][j]:
        newWord = currWord + grid[i+1][j]
        if trie.validPrefix(newWord):
            exploreWord(i+1, j, grid, visited, trie, newWord, foundWords)

    # explore left
    if j > 0 and not visited[i][j-1]:
        newWord = currWord + grid[i][j-1]
        if trie.validPrefix(newWord):
            exploreWord(i, j-1, grid, visited, trie, newWord, foundWords)

    # explore right
    if j < n-1 and not visited[i][j+1]:
        newWord = currWord + grid[i][j+1]
        if trie.validPrefix(newWord):
            exploreWord(i, j+1, grid, visited, trie, newWord, foundWords)

    visited[i][j] = False

main()
