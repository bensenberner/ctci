from string import ascii_lowercase as letters

def generateDefaultBoard():
    defaultLetterGrid = "raneudo"+\
                 "alodrat"+\
                 "terilwe"+\
                 "amopuam"+\
                 "lemimye"+\
                 "seopnas"+\
                 "mesicae"
    return defaultLetterGrid

def generateBoardFullAlphabet():
    board = ''
    curRow = letters
    for i in letters[:-1]:
        board += curRow + ','
        curRow = curRow[-1] + curRow[:-1]
    return board + curRow
