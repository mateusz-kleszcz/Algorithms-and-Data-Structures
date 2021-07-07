from random import randint


def findMedian(arr, l, r):
    n = r - l
    for i in range(n):
        j = i
        while j > 0 and arr[l + j - 1] > arr[l + j]:
            arr[l + j - 1], arr[l + j] = arr[l + j], arr[l + j - 1]
            j -= 1
    return arr[l + n // 2]


def medianMedians(arr, l, r):
    n = r - l
    if n <= 5: return findMedian(arr, l, r)
    medOfMed = [0] * ((n + 4) // 5)
    i = 0
    while i < n:
        lenOfSub = n % 5 if i + 5 > n else 5
        medOfMed[i // 5] = findMedian(arr, l + i, l + i + lenOfSub)
        i += 5
    return medianMedians(medOfMed, 0, len(medOfMed) - 1)


def partition(T, l, r, m):
    if l == r:
        i = l
    for i in range(l, r):
        if T[i] == m:
            break
    T[i], T[r] = T[r], T[i]
    i = l
    for j in range(l, r):
        if T[j] < m:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quickselect(T, l, r, k):
    n = len(T)
    if k > n: return -1
    p = partition(T, l, r, medianMedians(T, l, r))
    if p == k:
        return T[p]
    elif p > k:
        return quickselect(T, l, p - 1, k)
    else:
        return quickselect(T, p + 1, r, k)


tab = [12, 11, 13, 9, 2, 14, 1, 0, 15, 3, 8, 10, 4, 6, 16, 18, 7, 17, 5, 19]
print(quickselect(tab, 0, len(tab) - 1, 4))