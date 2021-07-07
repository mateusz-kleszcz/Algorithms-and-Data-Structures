from random import uniform, randint

MIN = 10
MAX = 20
n = 100

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


def insert(L, node):
    while L.next is not None and L.next.value < node.value:
        L = L.next

    node.next = L.next
    L.next = node


def insertionSort(L):
    S = Node()

    while L is not None:
        tmp = L.next
        L.next = None
        insert(S, L)
        L = tmp

    return S.next


def bucketSort(L):
    scope = MAX - MIN
    delta = n / scope

    buckets = [Node() for _ in range(n)]
    heads = buckets[:]

    while L is not None:
        index = int((L.value - MIN) * delta)
        tmp = L.next
        L.next = None
        buckets[index].next = L
        buckets[index] = buckets[index].next
        L = tmp

    newHead =  Node()
    newTail = newHead
    for i in range(n):
        if heads[i].next is not None:
            S = insertionSort(heads[i].next)
            newTail.next = S
            while newTail.next is not None:
                newTail = newTail.next

    return newHead.next


tab = [uniform(MIN, MAX - 0.01) for _ in range(n)]
print(tab)
L = tab2list(tab)
printList(bucketSort(L))