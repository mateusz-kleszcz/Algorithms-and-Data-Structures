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


def merge(L1, L2):
    L = None

    while L1 is not None and L2 is not None:
        if L1.value < L2.value:
            tmp = L1.next
            L1.next = L
            L = L1
            L1 = tmp
        else:
            tmp = L2.next
            L2.next = L
            L = L2
            L2 = tmp

    while L1 is not None:
        tmp = L1.next
        L1.next = L
        L = L1
        L1 = tmp

    while L2 is not None:
        tmp = L2.next
        L2.next = L
        L = L2
        L2 = tmp

    return L


A = tab2list([1, 3, 5])
B = tab2list([2, 6, 7, 10])
printList(merge(A, B))