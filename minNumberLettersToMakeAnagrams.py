from collections import Counter

def minNumberAnagrams(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    count = 0
    for letter in c1:
        if letter not in c2:
            count += c1[letter]
        else:
            count += abs(c1[letter] - c2[letter])
    return count

def main():
    s1 = 'abb'
    s2 = 'bbz'
    print(minNumberAnagrams(s1, s2))

main()
