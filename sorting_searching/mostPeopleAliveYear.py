def findBestYear(tups):
    n = len(tups)
    sortedBirths = sorted([x[0] for x in tups])
    sortedDeaths = sorted([x[1] for x in tups])

    b = d = 0
    numPeopleAlive = maxPeopleAlive = 0
    maxYearAlive = 1900
    while (b < n and d < n):
        if sortedBirths[b] < sortedDeaths[d]:
            numPeopleAlive += 1
            if numPeopleAlive > maxPeopleAlive:
                maxPeopleAlive = numPeopleAlive
                maxYearAlive = sortedBirths[b]
            b += 1
        elif sortedBirths[b] > sortedDeaths[d]:
            numPeopleAlive -= 1
            d += 1
        else:
            b += 1
            d += 1
    return maxYearAlive

if __name__ == "__main__":
    tups = [
            (1932, 1959),
            (1995, 2000),
            (1908, 1943),
            (1934, 1987),
            (1943, 1976),
            (1989, 1999),
            (1984, 1986),
            (1987, 1990),
    ]
    print(findBestYear(tups))
