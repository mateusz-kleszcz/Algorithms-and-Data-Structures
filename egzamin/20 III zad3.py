from zad3testy import runtests

class Node:
    def __init__(self):
        self.val = None
        self.next = None


def printList(L):
    while L is not None:
        print(L.val, '->', end=' ')
        L = L.next
    print('|')


def tab2list(T):
    H = Node()
    C = H
    for i in range(len(T)):
        X = Node()
        X.val = T[i]
        C.next = X
        C = X
    return H.next


def mergeTwo(L1, L2):

    merged = Node()
    head = merged

    while L1 is not None and L2 is not None:
        if L1.val < L2.val:
            nxt = L1.next
            L1.next = None
            merged.next = L1
            L1 = nxt
        else:
            nxt = L2.next
            L2.next = None
            merged.next = L2
            L2 = nxt
        merged = merged.next

    if L1 is not None:
        merged.next = L1
    if L2 is not None:
        merged.next = L2

    return head.next


def merge(tab):

    n = len(tab)
    isOdd = n % 2 and n > 1

    while n > 1:
        i = 0
        for i in range(0, n - 1, 2):
            new = mergeTwo(tab[i], tab[i + 1])
            tab[i // 2] = new
        if i + 1 == n:
            tab[i // 2] = tab[i]
        n = (n + 1) // 2

    if isOdd:
        return mergeTwo(tab[0], tab[- 1])

    return tab[0]


runtests(merge)