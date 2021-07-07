def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2


def heapify(T, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] > T[m]: m = l
    if r < n and T[r] > T[m]: m = r
    if m is not i:
        T[m], T[i] = T[i], T[m]
        heapify(T, n, m)


def buildHeap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)
    return T


def insertToHeap(heap, num):
    heap.append(num)
    n = len(heap) - 1
    while n > 0 and heap[parent(n)] < num:
        heap[parent(n)], heap[n] = heap[n], heap[parent(n)]
        n = parent(n)


heap = []
insertToHeap(heap, 40)
print(heap)