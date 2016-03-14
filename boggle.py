from python_datastructs import Trie
from boggleBoardGenerator import generateBoardFullAlphabet

def main():
    # build the trie
    with open('/usr/share/dict/words', 'r') as f:
        # the [:-1] omits the newline chars
        wordSet = set([word.lower()[:-1] for word in f.readlines()[:]])
        trie = Trie.Trie()
        trie.insertList(wordSet)

    ### preloaded board
    # letterGrid = "raneudo,"+\
    #              "alodrat,"+\
    #              "terilwe,"+\
    #              "amopuam,"+\
    #              "lemimye,"+\
    #              "seopnas,"+\
    #              "mesicae"

    ### user-defined board
    # print("Please enter comma separated lines of the grid:\n")
    # letterGrid = input()

    ### externally generated board
    letterGrid = generateBoardFullAlphabet()
    grid = convertGrid(letterGrid)
    foundWords = set()
    solveBoggle(grid, trie, foundWords)

    longestWords = sorted(list(foundWords), reverse=True, key=len)

    # print results
    for line in grid:
        print(line)
    for longWord in longestWords[:50]:
        print(longWord)

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

    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if isValid(x, y, i, j, m, n) and not visited[x][y]:
                newWord = currWord + grid[x][y]
                if trie.validPrefix(newWord):
                    exploreWord(x, y, grid, visited, trie, newWord, foundWords)

    visited[i][j] = False

def isValid(x, y, i, j,  m, n):
    return True if not (x == i and y == j) and x >= 0 and y >= 0 and x < m and y < n else False

if __name__ == "__main__":
    main()
