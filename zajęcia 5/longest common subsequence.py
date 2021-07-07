def printSolution(A, F, maximum, i, j):
    while F[i - 1][j] == maximum:
        if i - 1 == 0: break
        i -= 1
    while F[i][j - 1] == maximum:
        if j - 1 == 0: break
        j -= 1
    if i - 1 != 0 and j - 1 != 0:
        printSolution(A, F, maximum - 1, i - 1, j - 1)
    print(A[i - 1], end=' ')


def longest(A, B):
    n = len(A)

    F = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])

    printSolution(A, F, F[n][n], n, n)
    print()

    return F[n][n]


a = [7, 3, 1, 4, 2, 0]
b = [4, 2, 0, 7, 3, 1]
print(longest(a, b))