# find all palindromic partitions

# n i t i n
# n iti n
# nitin

def enumerateAllSubstrings(string, k):
    if k == 0:
        print(string)
        return

    for i in range(k):
        for j in range(len(string) - k):
            newString = ''.join(string[j:j+k])
            enumerateAllSubstrings(string[:j] + [newString] + [string[j+k:]], k - 1)

skrt = ['a', 'n', 'd']
enumerateAllSubstrings(skrt, 2)
