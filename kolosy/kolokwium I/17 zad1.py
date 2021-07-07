from math import ceil

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
    return H


def getLength(L):
    counter = -1
    while L is not None:
        L = L.next
        counter += 1
    return counter


def insertIntoBucket(bucket, node):
    while bucket.next is not None:
        bucket = bucket.next
    bucket.next = node


def insertMin(L, node):
    while L.next is not None and L.next.value < node.value:
        L = L.next
    node.next = L.next
    L.next = node


def insertSort(L):
    S = Node()
    L = L.next

    while L is not None:
        tmp = L.next
        insertMin(S, L)
        L = tmp
    return S


def sort(L):
    n = getLength(L)
    minVal = 0
    maxVal = 9
    scope = maxVal - minVal
    part = scope / n
    part = round(part, 1)
    l = ceil(scope / part)
    buckets = [Node() for _ in range(l)]

    curr = L.next
    while curr is not None:
        tmp = curr.next
        index = int(curr.value / part)
        curr.next = None
        insertIntoBucket(buckets[index], curr)
        curr = tmp

    S = Node()
    L = S
    for bucket in buckets:
        bucket = insertSort(bucket)
        S.next = bucket.next
        while S.next is not None:
            S = S.next

    return L


tab = [2, 4, 7, 5, 1, 3, 4]
L = tab2list(tab)
L = sort(L)
printList(L)