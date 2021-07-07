def printSolution(P, i):
    if P[i][0] != -1:
        printSolution(P, P[i][0])
        print(P[i][1], end=' ')


# def coins(T, s):
#     sums = [99999] * (s + 1)
#     parents = [[-1, -1] for _ in range(s + 1)]
#     sums[0] = 0
#     n = len(T)
#
#     for i in range(n):
#         for k in range(1, s + 1):
#             value = T[i]
#             minimum = sums[k]
#             if not k % value:
#                 if k / value < minimum:
#                     minimum = k / value
#                     parents[k][0] = k - value
#                     parents[k][1] = value
#             if k - value >= 0 and sums[k - value] + 1 < minimum:
#                 minimum = sums[k - value] + 1
#                 parents[k][0] = k - value
#                 parents[k][1] = value
#             sums[k] = minimum
#
#     print(sums)
#
#     printSolution(parents, s)
#     print()
#
#     return int(sums[s])


def coins(T, s):
    n = len(T)
    F = [[0] * (s + 1) for _ in range(n + 1)]




T = [8, 5, 1]
print(coins(T, 15))