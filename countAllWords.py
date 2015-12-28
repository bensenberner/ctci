OUT = 0
IN = 1
separators = set([' ', '\n', '\t'])

def countAllWords(string):
    state = OUT
    count = 0

    for i in range(len(string)):
        if string[i] in separators:
            state = OUT

        elif state == OUT:
            state = IN
            count += 1

    return count

print(countAllWords('asd oisa diofjasoidfaos idfjaois dfoiasj dofiajsdoif jaoisdjfasefjaiosdfias doasjifo asdiofjaoisjefoiajsefa'))
