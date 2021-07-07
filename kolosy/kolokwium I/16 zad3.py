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


def insert(L, Node):
    p = None
    c = L
    while c is not None:
        if c.value > Node.value:
            if p is not None:
                Node.next = c
                p.next = Node
            else:
                Node.next = c
                L = Node
            return L
        p = c
        c = c.next


def fixedSortedList(L):
    p = None
    c = L
    n = L.next
    while n is not None:
        if c.value > n.value:
            if n.value > p.value:
                p.next = n
                insert(L, c)
                return L
            else:
                c.next = n.next
                return insert(L, n)
        else:
            p = c
        c = n
        n = n.next
    return L


L = tab2list([9, 17, 28, 11, 31, 40])
printList(L)
P = fixedSortedList(L)
printList(P)