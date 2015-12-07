def matrixChainMult(arr):
    n = len(arr)
    dp = [[0 for x in range(n)] for y in range(n)]

    # 'length' represents the length of the subchain of matrices which is being
    # optimized, from 2 (since 1 is trivial) up until length n
    for length in range(2, n):

        # we iterate all start indices from 1 (since arr[i-1] represents the
        # first dimension of an index) up to n - length + 1, which would be the
        # last possible place for the start index of a matrix chain of this length
        # because after that, the chain would exceed the length of the input array
        for startIndex in range(1, n - length + 1):

            # end index is, appropriately, a distance "length" away from the start
            # index.
            endIndex = startIndex + length - 1

            # initialize the current table cell, representing the MIN number of
            # multiplications necessary to produce the matrix that was formed from
            # the matrices that span 'startIndex' to 'endIndex'
            dp[startIndex][endIndex] = float('inf')

            # splitIndex represents all possible ways of splitting the range of
            # matrices 'startIndex' to 'endIndex'. Keep in mind that since we are
            # incrementally growing "length", then all submatrices that are formed
            # by splitting 'startIndex' and 'endIndex' at 'splitIndex' have already
            # been optimized in the table.
            for splitIndex in range(startIndex, endIndex):

                # for every possible split between startIndex and endIndex,
                # determine the number of multiplications that are necessary to
                # produce the matrices that spans all of startIndex and endIndex
                currNumMults = \

                        # first number represents the number of multiplications
                        # needed to produce the matrix to the left of the split
                        dp[startIndex][splitIndex] + \

                        # second number represents the number of multiplications
                        # needed to produce the matrix at the right of the split
                        dp[splitIndex+1][endIndex] + \

                        # third number represents number of multiplications needed
                        # to multiply those two matrices together. We ignore all
                        # the numbers inbetween because those dimensions are dot
                        # product'd away during the intermediate multiplications.
                        arr[startIndex-1] * arr[splitIndex] * arr[endIndex]

                # find the minimum number of multiplications needed to produce the
                # matrix that spans the range startIndex, endIndex
                dp[startIndex][endIndex] = min(currNumMults, \
                                                dp[startIndex][endIndex])

    # dp[1][n-1] represents the minimum number of multiplications needed to produce
    # the matrix that is produced after multiplying all the other interior matrices
    # together. Thus, we can return this.
    return dp[1][n-1]

print(matrixChainMult([1, 2, 3, 5, 6, 7, 8, 9, 23]))
