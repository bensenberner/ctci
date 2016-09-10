def generateMapping(first, second, result, mapping):
    unsetLetter = findUnassignedLetter(mapping)
    # all of the letters have been assigned some value
    if unsetLetter == "":
        return checkMapping(first, second, result, mapping)

    # try every possible value
    for possibleValue in range(10):
        # check to see if we have already used this value
        if validAssignment(mapping, possibleValue):
            # try setting the currently chosen unset letter to some value
            mapping[unsetLetter] = possibleValue
            # see if setting this letter to this value ends up working
            if generateMapping(first, second, result, mapping):
                return True
            # if not (meaning that at some point, some letter was assigned
            # every possible value and none of them worked), then that means
            # that this current assignment to this current letter does not
            # work. Thus, we must unset it once again
            mapping[unsetLetter] = None

    # after trying all possible values for the chosen unset letter, none of
    # them wound up being successful. We return false to indicate that,
    # somewhere up the recursive chain, there was an incorrect assignment
    return False

def findUnassignedLetter(mapping):
    for letter in mapping:
        if mapping[letter] is None:
            return letter
    return ""

def validAssignment(mapping, num):
    return num not in mapping.values()

def checkMapping(first, second, result, mapping):
    addition = 0
    for num in [first, second]:
        multiplier = 1
        for i in range(len(num)-1, -1, -1):
            addition += mapping[num[i]] * (multiplier)
            multiplier *= 10

    sum = 0
    multiplier = 1
    for i in range(len(result)-1, -1, -1):
        sum += mapping[result[i]] * (multiplier)
        multiplier *= 10

    return addition == sum

if __name__ == "__main__":
    word1 = word2 = "ONE"
    result = "TWO"
    #mapping = {
    #        "F": 1,
    #        "U": 2,
    #        "N": 3,
    #        "L": 4,
    #        "A": 6,
    #}
    allLetters = set(list(word1) + list(word2) + list(result))
    mapping = {letter: None for letter in allLetters}
    generateMapping(word1, word2, result, mapping)
    print(mapping)
