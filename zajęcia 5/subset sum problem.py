def subset(A, t):
    n = len(A)
    F = [[False] * (t + 1) for _ in range(n)]
    for i in range(n):
        F[i][0] = True
    for i in range(n):
        for j in range(1, t + 1):
            if A[i] > j:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = F[i - 1][j] or F[i - 1][j - A[i]]

    for i in range(n):
        print(F[i])

    return F[n - 1][t]


tab = [3, 4, 5, 2]
t = 6
print(subset(tab, t))