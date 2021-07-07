def count(F, P, i, j):

    if F[i][j] != None:
        return F[i][j]

    minimum = float('inf')
    for k in range(i):
        index = j + i - k - P[i]
        if index >= 0 and index < len(P):
            value = count(F, P, k, j + i - k - P[i]) + 1
            if value < minimum:
                minimum = value

    F[i][j] = minimum

    return minimum


def frog(P):
    n = len(P)

    F = [[None] * n for _ in range(n)]
    F[0][P[0]] = 0
    minimum = float('inf')
    for i in range(n):
        jumps = count(F, P, n - 1, i)
        if jumps < minimum:
            minimum = jumps

    return minimum


A = [2, 2, 1, 0, 0, 0]
print(frog(A))
A = [4, 5, 2, 4, 1, 2, 1, 0]
print(frog(A))