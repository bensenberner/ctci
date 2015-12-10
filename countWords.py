def countWords(string):
    prevChar = string[0]
    count = 0 if prevChar is ' ' else 1
    for char in string[1:]:
        if prevChar is ' ' and char is not ' ':
            count += 1
        prevChar = char
    return count

string = ' a  b c db efa    a '
print(countWords(string))
