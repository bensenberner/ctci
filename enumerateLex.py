def nextPermutation(string):
    arr = list(string)
    # i marks off the non-decreasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    # less than necessary in case of an empty string
    # 0 represents that the whole string is non-decreasing, which means that
    # no more permutations can be made
    if i <= 0:
        return ''

    # Whatever i - 1 is, it has to be less than i, as i marks off the
    # non-decreasing subinterval. It also has to be the number that needs to be
    # swapped somewhere into the non-decreasing subinterval. We want to swap the
    # smallest number possible out of the subinterval, so that the number in the
    # i - 1th place is as small as possible, making the jump to the next permutation
    # as small as possible. So, we search from the right to the left (going from
    # lowest to highest), and the first number we see that is bigger than (i-1) is
    # the smallest number in the subinterval that we can swap out
    j = len(arr) - 1
    while j > 0 and arr[j] <= arr[i - 1]:
        j -= 1

    # now we can swap out the smallest possible number from the subinterval with
    # the i-1th number that will increment the whole number
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # now the i-1th number is larger than it was before (but the amount to which it
    # increased was as small as we were able to increase it), and so the non-decreasing
    # suffix can be reversed, which makes it as lexigraphically small as possible

    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    string = ''.join(arr)
    return string

a = input()
while (True):
    print(a)
    a = nextPermutation(a)
    if not a:
        break
