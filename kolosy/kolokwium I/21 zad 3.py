def insertion(tab):
    n = len(tab)
    for i in range(1, n):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab


def SortTab(T, P):
    n = len(T)

    buckets = [[] for _ in range(n)]

    for i in range(n):
        x = int(T[i] - 1)
        buckets[x].append(T[i])

    result = []

    for i in range(n):
        bucket = buckets[i]
        k = len(bucket)
        newBuckets = [[] for _ in range(k)]

        for el in bucket:
            delta = int((el - i - 1) * k)
            newBuckets[delta].append(el)

        for newBucket in newBuckets:
            insertion(newBucket)
            result += newBucket

    for i in range(n):
        T[i] = result[i]