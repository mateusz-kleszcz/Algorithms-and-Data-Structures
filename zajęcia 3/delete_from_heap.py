def left(i): return i * 2 + 1
def right(i): return i * 2 + 2
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


def deleteTopNode(heap):
    n = len(heap) - 1
    i = 0
    heap[i] = heap[n]
    del heap[n]
    n -= 1
    while left(i) <= n:
        l = left(i)
        r = right(i)
        print(heap, l, r)
        if r > n or heap[l] > heap[r]:
            heap[i], heap[l] = heap[l], heap[i]
            i = left(i)
        else:
            heap[i], heap[r] = heap[r], heap[i]
            i = right(i)


tab = [21, 37, 41]
buildHeap(tab)
print(tab)
deleteTopNode(tab)
print(tab)