P = [60, 100, 120]
W = [10, 20, 30]
maxW = 50
n = len(W)
F = [[-1] * (maxW + 1) for i in range(n)]

def knapsack(P, W, w, i):

    if w == 0:
        return 0
    if i == 0:
        if W[0] > w: return 0
        else: return W[0]
    if F[i][w] != -1:
        return F[i][w]

    if w >= W[i]:
        F[i][w] = max(
            knapsack(P, W, w, i - 1),
            knapsack(P, W, w - W[i], i - 1) + P[i]
        )
    else:
        F[i][w] = knapsack(P, W, w, i - 1)

    return F[i][w]


print(knapsack(P, W,  50, n - 1))