from random import randint
k = 10
n = 10

def getDigit(num, x):
    return (num % (10 ** (x + 1))) // (10 ** x)


def countingDescend(T, a):
    counters = [0] * 10
    for el in T:
        x = getDigit(el, a)
        counters[x] += 1
    for i in range(1, 10):
        counters[i] += counters[i - 1]

    sorted = [0] * n
    for i in range(n):
        x = getDigit(T[i], a)
        counters[x] -= 1
        sorted[counters[x]] = T[i]

    for i in range(n // 2):
        sorted[i], sorted[n - i - 1] = sorted[n - i - 1], sorted[i]

    return sorted


def countingAscend(T, a):
    counters = [0] * 10
    for el in T:
        x = getDigit(el, a)
        counters[x] += 1
    for i in range(1, 10):
        counters[i] += counters[i - 1]

    sorted = [0] * n
    for i in range(n - 1, -1, -1):
        x = getDigit(T[i], a)
        counters[x] -= 1
        sorted[counters[x]] = T[i]

    return sorted


def radixSort(T):
    for i in range(4):
        if i % 2 == 0:
            T = countingDescend(T, i)
        else:
            T = countingAscend(T, i)
    return T


tab = [7380, 6345, 7381, 7284, 7080, 7115, 7234, 7000, 7001, 7560]
print(tab)
print(radixSort(tab))