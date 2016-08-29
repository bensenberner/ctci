'''
Given a list of people with their birth and death years,
implement a method to compute the year with the most number of people alive.
You may assume that all people were born between 1900 and 2000 inclusive.

list of tuples, first number being birth year, second number being death year

solution 1:
make an array of size 101
each one representing a person who is alive
go through every person, increment all years in the range in which they were alive
go through the array, find the max
n people, this will take O(102n) time
'''

def mostLivingPeopleYearNaive(bdyears):
    years = [0 for x in range(102)]
    for bdyear in bdyears:
        birth, death = bdyear
        for year in range(birth, death+1):
            years[year] += 1
    maxYear = 0
    maxPeople = 0
    for i in range(len(years)):
        if years[i] > maxPeople:
            maxYear = i
            maxPeople = years[i]
    return maxYear

def mostLivingPeopleYear(bdyears):
    sortedByears = sorted(bdyear[0] for bdyear in bdyears)
    sortedDyears = sorted(bdyear[1] for bdyear in bdyears)
    n = len(bdyears)
    birthIdx = 0
    deathIdx = 0
    currCount = 0
    maxCount = 0
    maxYear = 0
    while (birthIdx < n and deathIdx < n):
        if sortedByears[birthIdx] < sortedDyears[deathIdx]:
            currCount += 1
            if currCount > maxCount:
                maxCount = currCount
                maxYear = sortedByears[birthIdx]
            birthIdx += 1
        else:
            currCount -= 1
            deathIdx += 1

    return maxYear

if __name__ == "__main__":
    bdyears = [(0, 70), (8, 20), (23, 93), (40, 70), (5, 55), (3, 88), (2, 22), (70, 90), (9, 11)]
    print(mostLivingPeopleYear(bdyears))
