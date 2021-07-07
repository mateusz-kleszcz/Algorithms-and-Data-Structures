from random import randint

class Node:
    def __init__(self):
        self.value = Node
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


def getTail(L):
    curr = L
    while curr.next is not None:
        curr = curr.next
    return curr


def parition(L):
    pivot = getTail(L)

    HL = None
    TP = pivot
    HR = Node()
    TR = HR

    prev = None
    curr = L

    while curr is not None and curr is not pivot:
        if curr.value < pivot.value:
            if HL is None:
                HL = curr
            prev = curr
            curr = curr.next
        elif curr.value == pivot.value:
            tmp = curr.next
            curr.next = None
            TP.next = curr
            TP = TP.next
            if prev is not None: prev.next = tmp
            curr = tmp
        else:
            tmp = curr.next
            curr.next = None
            TR.next = curr
            TR = TR.next
            if prev is not None: prev.next = tmp
            curr = tmp

    if prev is not None: prev.next = None

    return HL, pivot, HR.next


def quicksort(L):
    if L is None or L.next is None:
        return L

    newHead = None
    HL, HP, HR = parition(L)

    if HL is not None and HL is not HP: newHead = quicksort(HL)

    if newHead is None: newHead = HP
    else: getTail(newHead).next = HP

    if HR is not None: getTail(newHead).next = quicksort(HR)

    return newHead



tab = [randint(1, 10) for _ in range(10)]
L = tab2list(tab)
printList(L)
S = quicksort(L)
printList(S)