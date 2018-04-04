from collections import Counter
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in S.
'''
# LET"S ASSUME THE LETTERS IN T ARE UNIQUE
def minWindow(s, t):
    def check_can_contain_t(full_counter, t_counter):
        for key in t_counter:
            if full_counter[key] < t_counter[key]:
                return False
        return True

    t_counter = Counter(list(t))
    c = Counter()
    start_idx = 0
    original_end_idx = 0
    can_contain_t = False
    for idx, char in enumerate(s):
        c[char] += 1
        original_end_idx= idx
        if check_can_contain_t(c, t_counter):
            can_contain_t = True
            break

    if not can_contain_t:
        return ""

    min_start, min_end = start_idx, original_end_idx
    # find the smallest window
    while True and start_idx <= original_end_idx:
        curr_start_char = s[start_idx]
        if c[curr_start_char] == t_counter[curr_start_char]:
            break
        # move the curr_start_idx forward if it won't break the window
        c[curr_start_char] -= 1
        start_idx += 1
    for new_end_idx in range(original_end_idx, len(s)):
        # move the starting char as far up as possible without making the range
        # invalid
        while start_idx <= new_end_idx:
            curr_start_char = s[start_idx]
            if c[curr_start_char] == t_counter[curr_start_char]:
                break
            # move the curr_start_idx forward if it won't break the window
            c[curr_start_char] -= 1
            start_idx += 1

        c[s[new_end_idx]] += 1
        if (new_end_idx - start_idx) < (min_end - min_start):
            min_start, min_end = start_idx, new_end_idx

    while start_idx < len(s):
        curr_start_char = s[start_idx]
        if c[curr_start_char] == t_counter[curr_start_char]:
            break
        c[curr_start_char] -= 1
        start_idx += 1
    if (len(s) - 1 - start_idx) < (min_end - min_start):
        min_start, min_end = start_idx - 1, len(s) - 1
    return s[min_start:min_end+1]

print(minWindow("bba", "ab"))
