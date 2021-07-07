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


def dominance(P):
    n = len(P)
    S = []

    X = [0] * n
    Y = [0] * n
    for i in range(n):
        X[i] = (P[i][0], P[i][1], i)
        Y[i] = (P[i][0], P[i][1], i)

    quicksort(X, 0, n - 1, 0)
    quicksort(Y, 0, n - 1, 1)

    print(X)
    print(Y)

    Q = [[0] * 2 for _ in range(n)]
    for i in range(n):
        Q[X[i][2]][0] = i
        Q[Y[i][2]][1] = i

    print(Q)

    for i in range(n):
        if X[i] != -1:
            S.append(X[i][2])
            index = Q[X[i][2]][1]
            print(i, index)
            while index < n - 1:
                index += 1
                toDelete = Q[Y[index][2]][0]
                print(X[toDelete], toDelete)
                X[toDelete] = -1

    return S


P = [(2, 2), (1, 1), (2.5, 0.5), (3, 2), (0.5, 3)]
print(P)
print(dominance(P))