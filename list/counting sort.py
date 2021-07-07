from random import randint

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


def countingSort(L):

    counters = [Node() for _ in range(10)]
    heads = counters[:]

    while L is not None:
        tmp = L.next
        L.next = None
        counters[L.value].next = L
        counters[L.value] = counters[L.value].next
        L = tmp

    newHead = heads[0]
    newTail = counters[0]

    for i in range(1, 10):
        if heads[i].next is not None:
            newTail.next = heads[i].next
            newTail = counters[i]

    return newHead.next


tab = [randint(0, 9) for _ in range(10)]
L = tab2list(tab)
printList(countingSort(L))