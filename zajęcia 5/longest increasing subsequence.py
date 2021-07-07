# O(n^2)
def lis(A):
    n = len(A)

    F = [1] * n
    P = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    # printSolution(A, P, n - 1)
    print(F, P)
    return max(F)


def printSolution(A, P, i):
    if P[i] != -1:
        printSolution(A, P, P[i])
    print(A[i], end=' ')


# O(n*logn)
def better(T):
    n = len(T)

    F = [0] * (n + 1)
    P = [-1] * (n + 1)
    length = 1
    for i in range(1, n):
        if T[i] < T[F[0]]:
            F[0] = i
        elif T[i] > T[F[length - 1]]:
            P[i] = F[length - 1]
            F[length] = i
            length += 1
        else:
            l = 0
            r = length - 1
            while r - l > 1:
                m = l + (r - l) // 2
                if T[F[m]] > T[i]:
                    r = m
                else:
                    l = m
            P[i] = F[r - 1]
            F[r] = i

    # printSolution(T, P, n - 1)
    print(F, P)

    return length


tab = [2, 1, 4, 3]
print(tab)
print(lis(tab))
print(better(tab))