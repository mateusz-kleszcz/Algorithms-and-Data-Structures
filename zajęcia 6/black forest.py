def blackForrest(C):
    n = len(C)
    F = [0] * n
    F[0] = C[0]

    for i in range(1, n):
        F[i] = max(F[i - 2] + C[i], F[i - 1])

    return F[n - 1]


C = [7, 4, 4, 30, 11, 12, 81, 1, 19, 4]
print(blackForrest(C))