from collections import Counter
from string import ascii_lowercase as letters
'''
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.

Question: do these groups have to be in order? is this more of a "grouping" question than a "sorting" one?
do the groups have to be sorted internally or externally?

Things that define anagrams:
    they have the same letters
        two anagrams which have been individually sorted are identical
there are twenty six letters in the alphabet

naive way:
    create a dictionary: {string: sorted(string)} (assuming n is the average length of a string, and k is the number of strings, this will take O(k * n(log(n)))

    super naive:
        do selection sort on the dictionary. Start with a word, remember its value, search for that value in all other values in the dict, if you find a match, then put
        the matching value's key next to the original key. Comparing two values is O(n), comparing all values to all other values is O(k^2 * n)

    another way:
        sort the array by lexicographically the values in that dictionary, and sorting the corresponding keys in the array. Comparing two sorted strings will take O(n) time.
        sorting the strings will take O(k * n(log(n))) time
        dictionary + sorting array will take O(2k * n(log(n))) time

        PROBLEM: how to lexicographically compare two strings of different values?
            "ab" < "abb" ?
good way to do it:
    make a dictionary:
        {sorted(word) : [list containing every word that is the same sorted] }
        then just go through all the values and join them together into a list
'''

def sortAnagrams(words):
    d = {}
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in d:
            d[sortedWord] = [word]
        else:
            d[sortedWord].append(word)

    i = 0
    # rewrite the original array so that it has groups of sorted words together
    for sortWord in d:
        for word in d[sortWord]:
            words[i] = word
            i += 1

if __name__ == "__main__":
    words = ['cab', 'aab', 'abb', 'bac', 'cca', 'cac', 'aba']
    print(words)
    sortAnagrams(words)
    print(words)

