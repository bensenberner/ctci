d = {
        '0': ['a', 'b', 'c'],
        '1': ['d', 'e', 'f'],
        '2': ['g', 'h', 'i'],
        }

def enumFingers(inputString, currString, index, memo):
    if len(currString) == len(inputString):
        memo.append(currString)
    else:
        fingerPress = inputString[index]
        for possibleKey in d[fingerPress]:
            enumFingers(inputString, currString + possibleKey, index + 1, memo)

def main():
    inputstring = '00'
    memo = []
    enumFingers(inputstring, '', 0, memo)
    print(memo)

main()
