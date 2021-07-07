from random import randint

def partition(T, l, r):
    pivot = T[r]
    i = l
    for j in range(l, r):
        if T[j] < pivot:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quickselect(T, l, r, k):
    p = partition(T, l, r)
    if p == k:
        return
    if p > k:
        quickselect(T, l, p - 1, k)
    else:
        quickselect(T, p + 1, r, k)


def sumBetween(T, frm, to, n):
    quickselect(T, 0, len(T) - 1, frm)
    quickselect(T, frm, len(T) - 1, to)
    sum = 0
    for i in range(frm, to + 1):
        sum += T[i]
    return sum


tab = [randint(0, 100) for _ in range(10)]