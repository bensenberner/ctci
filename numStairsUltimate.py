"""
num_ways(2) -> [1,1] , [2] -> 2
num_ways(3) -> [1,1,1], [2,1], [1,2] -> 3
num_ways(4) -> [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2] --> 5


"""

"""
simple method:
   time complexity: 2^n
   space complexity: n (number of stack calls)

index memoization method
    time complexity: n
    space complexity: n+1

current and previous method:
    time complexity: n
    space complexity: O(1)
"""

def num_ways(stairs):
    if stairs == 1:
        return 1
    if stairs == 2:
        return 2
    else:
        return num_ways(stairs - 1) + num_ways(stairs - 2)
    


def num_ways(stairs, stride=2):
    arr = [0] * (stairs + 1)
    arr[1] = 1
    
    for currStairNum in range(2, stairs + 1):
        for currStride in range(1, stride + 1):
            if not currStride > currStairNum:
                arr[currStairNum] += arr[currStairNum - currStride] 
                
def num_ways(stairs, stride=2):
    if stairs <= 0:
        return 0
    
    if stairs == 1:
        return 1
    
    val = 0
    for s in range(1, stride + 1):
        val += num_ways(stairs - s, stride)
    return val
        

def num_ways(stairs, stride=1, is_left_foot=true):
    if stairs <= 0:
        return [0, 0]
    
    if stairs == 1:
        return [1, 0] if is_left_foot else [0, 1]
    
    returnArr = [0, 0]
    for s in range(1, stride + 1):
        # pretending that += does element wise sum of 2 arrays instead of concatenation
        returnArr += num_ways(stairs - s, stride, not is_left_foot)
        
    return returnArr

def num_ways(stairs, stride=2, numLegs=2, currLeg=0):
    if stairs <= 0:
        return [0] * numLegs
    
    if stairs == 1:
        arr = [0] * numLegs
        arr[currLeg] = 1
        return arr
    
    returnArr = [0] * numLegs
    for s in range(1, stride + 1):
        # pretending that += does element wise sum of 2 arrays instead of concatenation

        returnArr += num_ways(stairs - s, stride, numLegs, (currLeg + 1) % numLegs)

    return returnArr


