def fillUtil(res, curr, n):
    # if we have reached curr as 0, then that means that we have successfully
    # placed all numbers from 0 to n. So, we are finished
    if curr == 0: return True

    # iterate through all possible positions to place the current number
    for i in range(2*n - curr - 1):
        # if we haven't filled in the current spot, nor the corresponding spot
        # that is "curr" distance away (which it has to be because that is in
        # the definition of the problem, then try filling it in
        if res[i] == 0 and res[i + curr + 1] == 0:
            # fill in the empty spots with the current number
            res[i] = res[i + curr + 1] = curr

            # if it is possible to fill in these spots, then if we recurse
            # downwards, it will work all the way through. so, return True,
            # since we have found a valid placement strategy
            if fillUtil(res, curr-1, n): return True

            # if the above line didn't work, then that means that our current
            # placement of the numbers must not have been right. Thus, we should
            # continue to iterate through the rest of the possible positions.

            # we must now 0 out the current positions so that they can be used for
            # future iterations (note that because of the if statement on top, we
            # will never walk on the toes of a recursive call further up that wrote
            # some indices, because we only test out spots that have not yet been
            # written to.
            res[i] = res[i + curr + 1] = 0
    return False

def main():
    n = 7
    res = [0] * (2 * n)
    if fillUtil(res, n, n):
        print(res)
    else:
        print('impossible')

main()
