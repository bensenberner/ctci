from boggle_board_generator import generateBoardFullAlphabet
from boggle_board_generator import generateDefaultBoard
from itertools import zip_longest
from math import ceil, sqrt
from python_datastructs import Trie
import argparse

def main(letterGrid):
    # TODO: pickle this
    # build the trie
    with open('/usr/share/dict/words', 'r') as f:
        # the [:-1] omits the newline chars
        wordSet = set([word.lower()[:-1] for word in f.readlines()[:] if
            len(word) > 3])
        trie = Trie.Trie()
        trie.insertList(wordSet)

    n = ceil(sqrt(len(letterGrid)))
    grid = grouper(letterGrid, n)
    foundWords = set()
    solveBoggle(grid, trie, foundWords)

    longestWords = sorted(list(foundWords), reverse=True, key=len)

    # print results
    for line in grid:
        print(line)
    for longWord in longestWords[:50]:
        print(longWord)

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

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return list(zip_longest(*args, fillvalue=fillvalue))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enter a boggle board as one line')
    parser.add_argument('--board', help='input a board (default: returns a premade board)')
    args = parser.parse_args()
    board = args.board if args.board else getDefaultBoard()
    main(board)
