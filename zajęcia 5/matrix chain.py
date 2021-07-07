def matrixChain(A):
    n = len(A)
    L = [[0] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(0, n - i):
            min = 99999999
            # print(j, j + i)
            for k in range(j, j + i):
                # print('eee', k)
                # print(L[j][k], L[k + 1][j + i], A[j][0], A[k][1], A[j + i][1])
                new = L[j][k] + L[k + 1][j + i] + A[j][0] * A[k][1] * A[j + i][1]
                if new < min:
                    min = new
            L[j][j + i] = min

    return L[n - 1][n - 1]


A = [(5, 4), (4, 6), (6, 2), (2, 7)]
matrixChain(A)