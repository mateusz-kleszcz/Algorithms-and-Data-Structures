class Node:
    def __init__(self):
        self.value = None
        self.next = None


def tab2list(T):
    H = Node()
    C = H
    for i in range(len(T)):
        X = Node()
        X.value = T[i]
        C.next = X
        C = X
    return H.next


def printList(L):
    while L is not None:
        print(L.value, '->', end=' ')
        L = L.next
    print('|')


def cutList(L):
    if L is None:
        return None

    while L.next is not None and L.value <= L.next.value:
        L = L.next

    H = L.next
    L.next = None

    return H


def merge(L1, L2):
    H = Node()
    T = H

    while L1 is not None and L2 is not None:
        if L1.value < L2.value:
            T.next = L1
            L1 = L1.next
        else:
            T.next = L2
            L2 = L2.next
        T = T.next

    if L1 is None: T.next = L2
    if L2 is None: T.next = L1

    return H.next


def mergeSort(L):
    if L is None:
        return None

    while True:
        ST = Node()
        SH = ST
        while L is not None:
            H2 = cutList(L)
            H1 = L
            if SH.next is None and H2 is None:
                return L
            if H2 is None:
                ST.next = H1
                while ST.next is not None: ST = ST.next
                break
            T = cutList(H2)
            M = merge(H1, H2)
            ST.next = M
            while ST.next is not None: ST = ST.next
            L = T
        L = SH.next


T = [1, 2, 3, 6, 8, 7, 9, 11, 6, 7, 3, 4, 2]
L = tab2list(T)
printList(L)
S = mergeSort(L)
printList(S)