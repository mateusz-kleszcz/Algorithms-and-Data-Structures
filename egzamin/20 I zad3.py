def insertion(tab):
    n = len(tab)
    for i in range(1, n):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key


def fast_sort(tab, a):
    n = len(tab)
    delta = (a - 1) / n
    buckets = [[] for _ in range(n)]

    for el in tab:
        if el == a:
            index = n - 1
        else:
            index = int((el - 1) / delta)
        buckets[index].append(el)

    tab = []
    for bucket in buckets:
        insertion(bucket)
        tab += bucket

    return tab


T2 = [0.9, 0.7, 0.7, 0.5, 0.3, 0.2, 0.9]
D2 = [2**x for x in T2]
print(fast_sort(D2, 2))