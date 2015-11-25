MAX_CHARS = 26

# finds the number of unique characters, calculates if the string
# has at most k unique characters
def isValid(counts, k):
    for count in counts:
        if counts[count] > 0:
            val += 1
    return (k >= val)

def kUniques(s, k):
    uniqueChars = 0
    n = len(s)
    counts = [0] * MAX_CHARS

    curr_start = 0
    curr_end = 0
    max_window_size = 1
    max_window_start = 1

    for i in range(n):

