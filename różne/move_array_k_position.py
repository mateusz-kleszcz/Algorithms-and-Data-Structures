def reverse(T, start, end):
    mid = (start + end + 1) // 2
    for i in range(start, mid):
        T[i], T[end + start - i] = T[end + start - i], T[i]


def move(T, k):
    n = len(T)
    reverse(T, 0, n - 1)
    reverse(T, 0, k - 1)
    reverse(T, k, n - 1)
    return T


tab = [21, 37, 420, 69, 13, 11]