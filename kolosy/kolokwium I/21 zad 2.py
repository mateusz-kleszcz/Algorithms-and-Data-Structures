from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None
    self.next = None


def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2


def heapify(T, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l].val < T[m].val: m = l
    if r < n and T[r].val < T[m].val: m = r
    if m is not i:
        T[m], T[i] = T[i], T[m]
        heapify(T, n, m)


def insertToHeap(heap, node):
    heap.append(node)
    n = len(heap) - 1
    while n > 0 and heap[parent(n)].val > node.val:
        heap[parent(n)], heap[n] = heap[n], heap[parent(n)]
        n = parent(n)


def deleteTopNode(heap):
    n = len(heap) - 1
    i = 0
    value = heap[i]
    heap[i] = heap[n]
    del heap[n]
    heapify(heap, n, i)

    return value


def SortH(p, k):

    pointer = p
    sortedList = Node()
    sortedHead = sortedList

    heap = []

    for i in range(k):
        curr = pointer
        pointer = pointer.next
        curr.next = None
        insertToHeap(heap, curr)

    while pointer is not None:
        curr = pointer
        pointer = pointer.next
        curr.next = None
        insertToHeap(heap, curr)

        sortedList.next = deleteTopNode(heap)
        sortedList = sortedList.next

    for i in range(len(heap)):
        sortedList.next = deleteTopNode(heap)
        sortedList = sortedList.next

    sortedList.next = None

    return sortedHead.next


runtests( SortH )