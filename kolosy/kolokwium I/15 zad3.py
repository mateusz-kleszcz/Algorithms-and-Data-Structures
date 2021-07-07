from random import randint
from math import log2, ceil


def binarySearch(T, k):
    l = 0
    r = len(T) - 1

    while l <= r:
        p = (l + r) // 2
        if T[p] == k:
            return p
        elif T[p] < k:
            l = p + 1
        else:
            r = p - 1

    return -1


def sortLogValues(T, n):
    logValues = ceil(log2(n))

    values = []
    counter = -1
    for el in T:
        x = binarySearch(values, el)
        if x == -1:
            values += [el]
            j = counter
            while j >= 0 and values[j] > el:
                values[j + 1] = values[j]
                j -= 1
            values[j + 1] = el
            counter += 1

    counters = [0] * logValues
    for el in T:
        x = binarySearch(values, el)
        counters[x] += 1
    for i in range(1, logValues):
        counters[i] += counters[i - 1]

    sorted = [0] * n
    for i in range(n):
        x = binarySearch(values, T[i])
        counters[x] -= 1
        sorted[counters[x]] = T[i]

    return sorted


n = 1000
T = [randint(1, ceil(log2(n))) for _ in range(n)]
print(sortLogValues(T, n))