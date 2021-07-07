from random import randint

def digitsInPos(num, n, p):
    num //= n ** p
    return num % n


def countingSort(T, p):
    n = len(T)
    counters = [0] * n
    for el in T:
        counters[digitsInPos(el, n, p)] += 1
    for i in range(1, len(T)):
        counters[i] += counters[i - 1]
    sorted = [0] * n
    for i in range(n - 1, -1, -1):
        d = digitsInPos(T[i], n, p)
        counters[d] -= 1
        sorted[counters[d]] = T[i]

    return sorted


def linearSort(T):
    sorted = T
    for i in range(2):
        sorted = countingSort(sorted, i)
    return sorted


tab = [randint(0, 1000000 ** 2) for i in range(1000000)]
sorted = linearSort(tab)
print(sorted)