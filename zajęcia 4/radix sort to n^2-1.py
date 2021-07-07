from random import randint

def getNumInBase(num, base, k): return num // (base ** k) % base


def countingSort(T, n, k):
    counters = [0] * n
    for el in T:
        counters[getNumInBase(el, n, k)] += 1
    for i in range(1, n):
        counters[i] += counters[i - 1]

    sorted = [0] * n
    for i in range(n - 1, -1, -1):
        num = getNumInBase(T[i], n, k)
        counters[num] -= 1
        sorted[counters[num]] = T[i]

    return sorted


def radixSort(T, n):
    for i in range(2):
        T = countingSort(T, n, i)
    return T


n = 99
tab = [randint(0, n ** 2 - 1) for _ in range(n)]
print(tab)
print(radixSort(tab, n))