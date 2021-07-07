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
        T[i], T[m] = T[m], T[i]
        heapify(T, n, m)


def buildHeap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)


def heapSort(T):
    n = len(T)
    buildHeap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)
        print(T)
    return T


tab = [21, 37, 69, 420, 11, 23, 56, 11]
print(heapSort(tab))