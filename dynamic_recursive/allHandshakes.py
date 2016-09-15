def numShakes(numMales, numFemales, male):
    if male:
        if numFemales == 0:
            return 0
        else:
            return(1 + numShakes(numMales - 1, numFemales, False))
    else:
        if numMales == 0:
            return 0
        else:
            return(1 + numShakes(numMales, numFemales - 1, True))

print(numShakes(100, 100, True))
