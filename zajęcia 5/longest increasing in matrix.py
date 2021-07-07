def liMemo(T, F, m, n, i, j, prev):
    if i < 0 or i >= n or j < 0 or j >= m or T[i][j] >= prev: return 0
    if F[i][j]: return F[i][j]
    F[i][j] = 1 + max(
        liMemo(T, F, m, n, i - 1, j, T[i][j]),
        liMemo(T, F, m, n, i + 1, j, T[i][j]),
        liMemo(T, F, m, n, i, j - 1, T[i][j]),
        liMemo(T, F, m, n, i, j + 1, T[i][j]),
    )
    return F[i][j]


def li(T, m, n):
    F = [[0] * m for _ in range(n)]
    maxi = - 1
    for i in range(m):
        for j in range(n):
            num = liMemo(T, F, m, n, i, j, 999999)
            if num > maxi: maxi = num

    for i in range(n):
        for j in range(m):
            if F[i][j] == maxi:
                k, l = i, j
                break

    print(T[k][l], end=' ')
    for i in range(maxi - 1, 0, -1):
        if k - 1 >= 0 and F[k - 1][l] == i:
            print(T[k - 1][l], end=' ')
            k -= 1
        elif l - 1 >= 0 and F[k][l - 1] == i:
            print(T[k][l - 1], end=' ')
            l -= 1
        elif k + 1 < n and F[k + 1][l] == i:
            print(T[k + 1][l], end=' ')
            k += 1
        elif l + 1 < m and F[k][l + 1] == i:
            print(T[k][l + 1], end=' ')
            l += 1


tab = [
    [13, 12, 0],
    [1, 11, 9],
    [3, 6, 8],
    [2, 4, 5],
]
li(tab, 3, 4)