def allSentences(allWords, currString, index):
    if index == len(allWords):
        print(currString)
        return

    for word in allWords[index]:
        newString = currString + word + ' '
        allSentences(allWords, newString, index + 1)

w = [['you', 'we'], ['have', 'are'], ['sleep', 'eat', 'drink']]
allSentences(w, '', 0)
