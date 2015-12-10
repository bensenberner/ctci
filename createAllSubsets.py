def createAllSubsets(arr, res):
    if not arr:
        return res
    if len(arr) == 1:
        res.append(arr)
        return res

    temp = createAllSubsets(arr[1:], res)
    tempLen = len(temp)

    for i in range(tempLen):
        temp.append([arr[0]] + temp[i])

    res.append([arr[0]])
    return temp

res = [[]]
createAllSubsets([1, 2, 3, 5, 6, 7, 8, 9], res)

target = 17
done = []
for subSet in res:
    if sum(subSet) == target:
        done.append(subSet)

print(done)
