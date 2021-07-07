def partition(T, l, r, k):
    pivot = T[r][k]

    i = l
    for j in range(l, r):
        if T[j][k] < pivot:
            T[i], T[j] = T[j], T[i]
            i += 1

    T[i], T[r] = T[r], T[i]
    return i


def quicksort(T, l, r, k):
    while l < r:
        pivot = partition(T, l, r, k)
        if pivot - l <= r - pivot:
            quicksort(T, l, pivot - 1, k)
            l = pivot + 1
        else:
            quicksort(T, pivot + 1, r, k)
            r = pivot - 1


def ranges(T):
    n = len(T)
    indexes = [[0, 0, 0] for _ in range(n)]
    for i in range(n):
        indexes[i][0] = T[i][0]
        indexes[i][1] = T[i][1]
        indexes[i][2] = i

    quicksort(indexes, 0, n - 1, 0)
    X = [0] * n
    for i in range(n):
        X[i] = (indexes[i][2], i)

    quicksort(indexes, 0, n - 1, 1)
    Y = [0] * n
    for i in range(n):
        Y[i] = (indexes[i][2], i)

    quicksort(X, 0, n - 1, 0)
    quicksort(Y, 0, n - 1, 0)

    max = -1
    maxIndex = -1
    for i in range(n):
        if X[i][1] - Y[i][1] > max:
            max = X[i][1] - Y[i][1]
            maxIndex = i

    return max, T[maxIndex]


T = [(2, 5), (3, 7), (1, 6), (3, 4)]
print(ranges(T))