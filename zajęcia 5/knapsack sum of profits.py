from math import ceil

def getSolution(F, W, P, i, p):
    if i < 0: return []
    if i == 0:
        if p != 0: return [0]
        return []
    if F[i][p] != F[i - 1][p]:
        return getSolution(F, W, P, i - 1, p - P[i]) + [i]
    return getSolution(F, W, P, i - 1, p)


# def knapsack(W, P, maxProfit, weight):
#     n = len(W)
#     F = [[0] * (maxProfit + 1) for _ in range(n)]
#
#     for p in range(1, maxProfit + 1):
#         F[0][p] = W[0] * ceil(p / P[0])
#
#     for i in range(1, n):
#         for j in range(1, maxProfit + 1):
#             F[i][j] = F[i - 1][j]
#             if j >= W[i]:
#                 F[i][j] = min(F[i][j], W[i] + F[i - 1][j - P[i]])
#
#     for i in range(maxProfit + 1):
#         if F[n - 1][i] > weight:
#             return i - 1
#     return 0


def knapsackWithoutRepeating(W, P, maxProfit, weight):
    n = len(W)
    F = [[99] * (maxProfit + 1) for _ in range(n)]

    for i in range(n):
        F[i][0] = 0

    cost = P[0]

    for i in range(1, maxProfit + 1):
        if P[0] >= i:
            F[0][i] = W[0]
        else: break

    for i in range(1, n):
        cost += P[i]
        for j in range(1, cost + 1):
            F[i][j] = F[i - 1][j]
            if j >= P[i]:
                F[i][j] = min(F[i][j], W[i] + F[i - 1][j - P[i]])
            else:
                F[i][j] = min(F[i][j], W[i])

    for i in range(n):
        print(F[i])

    for i in range(maxProfit + 1):
        if F[n - 1][i] > weight:
            print(getSolution(F, W, P, n - 1, i - 1))
            return i - 1
    return 0


P = [7, 10, 8, 4, 5, 3]
W = [13, 4, 5, 12, 9, 1]
print(knapsackWithoutRepeating(W, P, 37, 10))