class Node:
    def __init__(self):
        self.value = None
        self.next = None


def printList(L):
    while L is not None:
        print(L.value, '->', end=' ')
        L = L.next
    print('|')


def tab2list(T):
    H = Node()
    C = H
    for i in range(len(T)):
        X = Node()
        X.value = T[i]
        C.next = X
        C = X
    return H.next


def getMinAndMax(L):

    min = max = L.value

    while L is not None:
        if L.value < min:
            min = L.value
        if L.value > max:
            max = L.value
        L = L.next

    return min, max


def removeDuplicates(L):
    min, max = getMinAndMax(L)
    values = [0] * (max - min + 1)

    prev = None
    curr = L
    H = curr
    while curr is not None:
        if values[curr.value - min]:
            prev.next = curr.next
        else:
            values[curr.value - min] += 1
            prev = curr
        curr = curr.next

    return H


L = tab2list([5, 3, 4, 2, 5, 4, 1, 3])
printList(removeDuplicates(L))