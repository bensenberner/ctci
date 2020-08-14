def mergeKSortedLinkedLists(listArr):
    if len(listArr) == 0:
        return None
    elif len(listArr) == 1:
        return listArr[0]
    else:
        newListArr = []
        # odd length list
        if len(listArr) % 2 == 1:
            extraList = listArr._pop()
            listArr[-1] = mergeLists(listArr[-1], extraList)
        for i in range(1, len(listArr), 2):
            newListArr.append(mergeLists(listArr[i - 1], listArr[i]))
        return mergeKSortedLinkedLists(newListArr)


def mergeLists(list1, list2):
    newLinkedList = LinkedList()
    while not list1.isEmpty() and not list2.isEmpty():
        if list1.peek() < list2.peek():
            newLinkedList.add(list1._pop())
        else:
            newLinkedList.add(list2._pop())

    # empty remaining list, whichever one it is
    while not list1.isEmpty():
        newLinkedList.add(list1._pop())
    while not list2.isEmpty():
        newLinkedList.add(list2._pop())

    return newLinkedList
