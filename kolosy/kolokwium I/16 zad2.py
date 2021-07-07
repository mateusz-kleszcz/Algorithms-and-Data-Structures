#dzielimy liczby na 2 zbiory - parzyste i nieparzyste
#nieparzyste są już posortowane, sortujemy parzyste
#najlepiej quicksortem, skoro są duże i z nieznanym rozkładem
#scalamy te 2 posortowane tablice w jedną tak jak w megesorcie
#podzielenie na 2 podzbiory w czasie O(n), sortowanie to optymistycznie O(logn*log(logn)) czyli szybciej niż liniowo, scalanie w czasie O(n)
#czyli cały algorytm w czasie O(n)

from math import log2, ceil

def partition(T, l, r):
    x = T[r]
    i = l
    for j in range(l, r):
        if T[j] < x:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quicksort(T, l, r):
    while l < r:
        p = partition(T, l, r)
        if (p - l) <= (r - p):
            quicksort(T, l, p - 1)
            l = p + 1
        else:
            quicksort(T, p + 1, r)
            r = p - 1


def merge(T, T1, T2):
    i = 0
    j = 0
    while i < len(T1) - 1 and j < len(T2) - 1:
        if T1[i] < T2[j]:
            T[i + j] = T1[i]
            i += 1
        else:
            T[i + j] = T2[j]
            j += 1
    while i < len(T1):
        T[i + j] = T1[i]
        i += 1
    else:
        T[i + j] = T2[j]
        j += 1


def sort(T):
    n = len(T)
    odd = [0] * (n - ceil(log2(n)))
    even = [0] * ceil(log2(n))
    oddCounter = 0
    evenCounter = 0
    for el in T:
        if el % 2:
            odd[oddCounter] = el
            oddCounter += 1
        if not el % 2:
            even[evenCounter] = el
            evenCounter += 1
    quicksort(even, 0, len(even) - 1)
    merge(T, odd, even)


tab = [17, 52, 21, 12, 41, 24, 61, 83]
sort(tab)
print(tab)