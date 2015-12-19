def printTable(num):
    for i in range(1, num+1):
        string = ''
        for j in range(1, num+1):
            string += str(i * j) + '\t'
        print(string)

printTable(12)
