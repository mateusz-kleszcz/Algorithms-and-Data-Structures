def optimal(T):
    n = len(T)
    F = [[0] * n for _ in range(n)]

    sum = 0
    for el in T:
        sum += el

    for gap in range(n):
        for j in range(gap, n):
            i = j - gap

            x = 0
            if i + 2 <= j:
                x = F[i + 2][j]
            y = 0
            if i + 1 <= j - 1:
                y = F[i + 1][j - 1]
            z = 0
            if i <= j - 2:
                z = F[i][j - 2]
            F[i][j] = max(
                T[i] + min(x, y),
                T[j] + min(y, z)
            )

    for i in range(n):
        print(F[i])


arr1 = [ 8, 15, 3, 7 ]
print(optimal(arr1))