def partition(T, l, r, key):
    x = T[r][key]
    i = l - 1

    for j in range(l, r):
        if T[j][key] < x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, l, r, key):
    while l < r:
        p = partition(T, l, r, key)
        if p - l <= r - p:
            quicksort(T, l, p - 1, key)
            l = p + 1
        else:
            quicksort(T, p + 1, r, key)
            r = p - 1


def dominance(P):
    n = len(P)

    sortedByX = [(0, 0, 0)] * n # P posortowane po x, z indeksami z oryginału
    sortedByY = [(0, 0, 0)] * n # P posortowane po y, z indeksami z oryginału

    for i in range(n):
        x, y = P[i]
        sortedByX[i] = (x, y, i)
        sortedByY[i] = (x, y, i)

    # sortowanie o(nlogn)
    quicksort(sortedByX, 0, n - 1, 0)
    quicksort(sortedByY, 0, n - 1, 1)

    # pod jakim indeksem w tablicy x, y znajduje się punkt
    indexes = [(-1, -1)] * n
    for i in range(n):
        indexX = sortedByX[i][2]
        indexY = sortedByY[i][2]
        indexes[indexX] = (i, indexes[indexX][1])
        indexes[indexY] = (indexes[indexY][0], i)

    S = []

    end = n
    for i in range(n):
        if sortedByX[i] != -1:
            x = sortedByX[i][2]
            S.append(x)

            indexInY = indexes[x][1]
            if indexInY < end:
                for j in range(indexInY + 1, end):
                    numToDelete = sortedByY[j][2]
                    indexToDelete = indexes[numToDelete][0]
                    sortedByX[indexToDelete] = -1
                end = indexInY + 1

    return S