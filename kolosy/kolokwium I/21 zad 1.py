def getCoordinates(num, n):
    mid = (n ** 2) // 2
    first = mid - n // 2
    last = mid + (n - 1) // 2

    if num < first:
        x = (1 + (1 + 8 * num) ** (1 / 2)) / 2
        x = int(x)
        y = num - int(x * (x - 1) / 2)
        return x, y

    if first <= num <= last:
        x = num - first
        return x, x

    if last < num:
        num -= last + 1
        x = (1 + (1 + 8 * num) ** (1 / 2)) / 2
        x = int(x)
        y = num - int(x * (x - 1) / 2)
        return y, x


def partition(T, left, right):
    rightX, rightY = getCoordinates(right, len(T))
    pivot = T[rightX][rightY]
    i = left
    iX, iY = getCoordinates(i, len(T))
    for j in range(left, right):
        jX, jY = getCoordinates(j, len(T))
        if T[jX][jY] < pivot:
            T[iX][iY], T[jX][jY] = T[jX][jY], T[iX][iY]
            i += 1
            iX, iY = getCoordinates(i, len(T))
    T[iX][iY], T[rightX][rightY] = T[rightX][rightY], T[iX][iY]
    return i


def quickselect(T, left, right, k):
    if left == right:
        return

    pivot = partition(T, left, right)

    if k == pivot:
        return
    elif k > pivot:
        return quickselect(T, pivot + 1, right, k)
    else:
        return quickselect(T, left, pivot - 1, k)


def Median(T):

    n = len(T)

    mid = (n ** 2) // 2
    first = mid - n // 2
    last = mid + (n - 1) // 2

    quickselect(T, 0, (n ** 2) - 1, first)
    quickselect(T, 0, (n ** 2) - 1, last)

    return T


T = [ [ 2, 3, 5],
    [ 7,11,13],
    [17,19,23] ]

print(Median(T))