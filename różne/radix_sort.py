def digitInPos(num, pos): return (num % (10 ** (pos + 1))) // (10 ** pos)


def countingSort(T, digit):
    counters = [0] * 10
    for el in T:
        counters[digitInPos(el, digit)] += 1
    for i in range(1, 10):
        counters[i] += counters[i - 1]

    sorted = [0] * len(T)
    for i in range(len(T) - 1, -1, -1):
        d = digitInPos(T[i], digit)
        counters[d] -= 1
        sorted[counters[d]] = T[i]
    return sorted


def getMax(T):
    max = T[0]
    for el in T:
        if el > max:
            max = el
    return max


def digitsInNumber(num):
    counter = 0
    while num > 0:
        counter += 1
        num //= 10
    return counter


def radix_sort(T):
    maxDigits = digitsInNumber(getMax(T))
    sorted = T
    for i in range(maxDigits):
        sorted = countingSort(sorted, i)
    return sorted


tab = [63213, 312, 534, 584, 456, 245, 11356, 321, 12, 2, 1, 6969, 420]
print(radix_sort(tab))