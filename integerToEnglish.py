def translate(integer):
    strint = str(integer)
    # find groups of three
    highestNumLen = len(strint) % 3
    if len(strint) > 3:
        for i in range(len(strint) - 3, highestNumLen - 1, -3):
            num = strint[i:i+3]
            # now make create the hundreds and append depending on how big i is
translate(1234)
