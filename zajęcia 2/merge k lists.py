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


def merge(L1, L2):
    if L1 is None: return L2
    if L2 is None: return L1

    L = Node()
    H = L
    while L1 is not None and L2 is not None:
        if L1.value < L2.value:
            L.next = L1
            L1 = L1.next
        else:
            L.next = L2
            L2 = L2.next
        L = L.next

    while L1 is not None:
        L.next = L1
        L = L.next
        L1 = L1.next
    while L2 is not None:
        L.next = L2
        L = L.next
        L2 = L2.next

    return H.next


def mergeKList(pointers):
    j = len(pointers) - 1
    last = j
    while last != 0:
        i = 0
        while i < j:
            pointers[i] = merge(pointers[i], pointers[j])
            i += 1; j -= 1
            last = j

    return pointers[0]


A = tab2list([23, 37, 420])
B = tab2list([11, 15, 27])
C = tab2list([24, 30, 420])
L = mergeKList([A, B, C])
printList(L)