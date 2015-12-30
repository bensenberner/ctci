# Given two lists (of unique integers) in sorted (ascending) order,
# find their intersection.
# list 1 is of length n
# list 2 is of length m


# 3, 499, 500, 800, 1000
                                
# 800, 802, ... 1000
 
           
def findIntersectionLinear(list1, list2):
    res = set()
    
    i = 0
    j = 0
    while (i < len(list1) and j < len(list2)):
        if list1[i] == list2[j]:
            res.add(list1[i])
            i += 1
            j += 1
            
        elif list1[i] < list2[j]:
            i += 1
            
        else:
            j += 1
            
    return res

def findIntersectionBinarySearch(list1, list2):
    shortList, longList = list1, list2 if len(list1) < len(list2) else list2, list1
    
    res = set()
    startIndexShort = lowerBound(shortList, longList[0])
    
    endIndexShort = upperBound(shortList, longList[-1])
    endIndexLong = upperBound(longList, shortList[-1])
    
    for num in shortList[startIndexShort : endIndexShort]:
        startIndexLong = lowerBound(longList, num)
        if binarySearch(longList[startIndexLong : endIndexLong], num):
            res.add(num)
            
    return res
    
    
def binarySearch(listOfNums, num)
    '''input: listOfNums is a list of integers
       num is the integer that is being searched for in listOfNums
       return True if num is present in listOfNums else False'''
    
def lowerBound(listOfNums, num)
    '''input: listOfNums is a list of integers
       num is the integer that is being searched for in listOfNums
       if num is present in listOfNums, return its index in listOfNums
       else, return the lowest possible index in which  num could be inserted
       if ascending order were preserved'''
     
def upperBound(listOfNums, num)
    '''input: listOfNums is a list of integers
       num is the integer that is being searched for in listOfNums
       if num is present in listOfNums, return its index in listOfNums
       else, return the highest possible index in which  num could be inserted
       if ascending order were preserved'''