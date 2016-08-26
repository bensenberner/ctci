'''
take an array and print non overlapping in order pairs
input: 1234
output:
    (1234)
    (1)(234)
    (1)(23)(4)
    (1)(2)(34)
    (12)(34)
    (12)(3)(4)
    (123)(4)
    (1)(2)(3)(4)
'''

'''
1
(1)

12
(12)
(1)(2)
'''
def printAllParens(arr, idx, currString):
    if idx == len(arr):
        print(currString)

    else:
        for i in range(idx, len(arr)):
            prefix = arr[idx : i+1]
            printAllParens(arr, i+1, currString + '(' + prefix + ')' )

printAllParens('1234', 0, '')
