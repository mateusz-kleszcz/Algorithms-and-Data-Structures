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


def split(L):
    if L is None or L.next is None:
        return L

    E = None
    O = Node()
    HO = O
    prev = None
    curr = L
    while curr is not None:
        if curr.value % 2 == 0:
            if E is None: E = curr
            prev = curr
            curr = curr.next
        else:
            tmp = curr.next
            curr.next = None
            O.next = curr
            O = O.next
            if prev is not None: prev.next = tmp
            curr = tmp

    return E, HO.next


L = tab2list([4, 2, 0, 2, 1, 3, 7, 6, 9, 6, 9])
printList(L)
E, O = split(L)
printList(E)
printList(O)