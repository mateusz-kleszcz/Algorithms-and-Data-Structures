def printSolution(T, F, i, j):
    if i != 0 or j != 0:
        if i == 0:
            printSolution(T, F, i, j - 1)
        elif j == 0:
            printSolution(T, F, i - 1, j)
        elif F[i - 1][j] > F[i][j - 1]:
            printSolution(T, F, i, j - 1)
        else:
            printSolution(T, F, i - 1, j)
    print(T[i][j], end=' ')


def walk(T):
    n = len(T)

    F = [[0] * n for _ in range(n)]
    F[0][0] = T[0][0]
    for i in range(1, n):
        F[0][i] = F[0][i - 1] + T[0][i]
    for i in range(1, n):
        F[i][0] = F[i - 1][0] + T[i][0]

    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = min(F[i - 1][j], F[i][j - 1]) + T[i][j]

    printSolution(T, F, n - 1, n - 1)

    return F[n - 1][n - 1]


tab = [
    [10, 11, 15, 14],
    [12, 8, 92, 41],
    [17, 3, 1, 15],
    [19, 21, 37, 42],
]
print(walk(tab))