def linear_search(A, v):
    '''Loop invariant: the indices 0..i have been searched
    for v and do not contain it
    '''
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None
