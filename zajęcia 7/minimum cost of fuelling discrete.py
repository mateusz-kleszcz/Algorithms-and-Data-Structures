def printSolution(F, num, i):
    if i >= 0:
        if F[i] < num:
            printSolution(F, F[i], i - 1)
        else:
            printSolution(F, num, i - 1)
    if F[i] < num:
        print(F[i], end=' ')


def minimumCost(l, S, P):
    n = len(S)

    F = [float('inf')] * n
    F[0] = S[0] * P[0]

    for i in range(1, n):
        if S[i] <= l:
            F[i] = S[i] * P[i]
        j = i - 1
        while S[i] - S[j] <= l and j >= 0:
            cost = F[j] + P[i] * (S[i] - S[j])
            if cost < F[i]:
                F[i] = cost
            j -= 1

    printSolution(F, float('inf'), n - 1)

    return F[n - 1]


S = [0, 2, 4, 6, 9, 11, 13, 16, 18, 20, 25]
C = [0, 4, 3, 2, 3, 3, 5, 4, 2, 4, 0]
L = 7
minimumCost(L, S, C)