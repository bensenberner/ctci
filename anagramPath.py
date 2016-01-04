''' Given two words which are anagrams, consider that your task at hand is
to convert one word to the other only by swapping two adjacent characters,
one swap at a time. For example, for GOD --> DOG:
    GOD
    OGD
    ODG
    DOG
print out all the swaps necessary. Note that this does not necessarily have
to be the minimum number of swaps (do that for extra credit) but there shouldn't
be unnecessary cycles, e.g.
    GOD
    OGD
    ODG
    OGD
    ODG
    OGD
    ODG
    DOG
'''

def makePath(currStr, targetStr, currPath, returnVal, used):
    if currStr == targetStr:
        # weird stuff was happening wherein the currPath would be modified
        # and I didn't feel like doing recursive bugchecking so this works
        # it is essentially copy.deepcopy()
        for e in currPath:
            returnVal.append(e)
        return True

    # try all swaps
    for i in range(1, len(currStr)):
        newStr = swap(currStr, i - 1, i)

        # if that swap hasn't been used yet
        if newStr not in used:

            # test it out on the current path
            currPath.append(newStr)

            # add it to the list of swapstrings we've already used in this current path
            used.add(newStr)

            # if that worked, then great! return True
            if makePath(newStr, targetStr, currPath, returnVal, used):
                return True

            # otherwise, chop off the current swapstring from the current path and backtrack
            # (try another one)
            currPath = currPath[:-1]

    # we have tried all possible swaps on this string and none of them worked. That means we
    # gotta backtrack! remove this from the used list since we're going to return false on this
    # one and go back up
    used.remove(currStr)
    return False

def swap(string, i, j):
    l = list(string)
    l[i], l[j] = l[j], l[i]
    return ''.join(l)

def main():
    # to remove the possibility of doing an unnecessary number of swaps, we must
    # use a set to keep track of what we have attempted to use in this swap path
    used = set()
    str1 = 'LOIDEA'
    str2 = 'IOELDA'

    # for some reason, the path list sometimes gets modified even after the final swap is found.
    # this "returnVal" will solve the issue...for now
    returnVal = []

    # start things off right. Egg whites, bacon, and water.
    used.add(str1)
    path = [str1]
    print(makePath(str1, str2, path, returnVal, used))
    print(returnVal)

main()
