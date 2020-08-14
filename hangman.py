from string import ascii_lowercase
import random


def findMostUsedLetter(letter_dict):
    max_letter = ""
    max_count = 0
    for letter in letter_dict:
        wordcount = len(letter_dict[letter])
        if wordcount > max_count:
            max_letter = letter
            max_count = wordcount
    return max_letter


def prune_letter_dict(letter, l, correct):
    if correct:
        for letter in l:
            l[letter] = set([word for word in l[letter] if letter in word])
    else:
        l._pop(letter)
        for letter in l:
            l[letter] = set([word for word in l[letter] if not letter in word])


with open("/usr/share/dict/words", "r") as f:
    # the [:-1] omits the newline chars
    letter_dict = {letter: set() for letter in ascii_lowercase}
    for word in f.readlines():
        curr_word = word.lower()[:-1]
        if curr_word.isalpha():
            for letter in curr_word:
                letter_dict[letter].add(curr_word)

word = input("Please enter a word and I will try to guess it!\n")
letter_set = set(word)
num_guesses = 0
max_guesses = 10
while num_guesses <= max_guesses and len(letter_set) > 0:
    best_guess_letter = findMostUsedLetter(letter_dict)
    # guess was correct
    correct = best_guess_letter in letter_set
    print("I guessed", best_guess_letter, "and I was", correct)
    if correct:
        letter_set.remove(best_guess_letter)
    else:
        num_guesses += 1
    prune_letter_dict(best_guess_letter, letter_dict, correct)

print("You lose!")
