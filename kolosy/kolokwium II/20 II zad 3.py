def isDigit(a, b):
    countersA = [False] * 10
    countersB = [False] * 10

    while a > 0:
        countersA[a % 10] = True
        a //= 10

    while b > 0:
        countersB[b % 10] = True
        b //= 10

    for i in range(10):
        if countersA[i] and countersB[i]:
            return True

    return False


def memo(T, f, i, j, n, toCheck):

    if f[i][j] != float('inf'):
        return f[i][j]

    minimum = float('inf')
    for k in toCheck:
        value = memo(T, f, i, k, n) + memo(T, f, j, k, n)
        if value < minimum:
            minimum = value
    f[i][j] = minimum
    f[j][i] = minimum

    return f[i][j]

def minCost(T):
    n = len(T)

    f = [[float('inf')] * n for _ in range(n)]

    minimum = T[0]
    minIndex = 0
    maximum = T[0]
    maxIndex = 0
    for i in range(n):
        if T[i] < minimum:
            minimum = T[i]
            minIndex = i
        if T[i] > maximum:
            maximum = T[i]
            maxIndex = i
        for j in range(n):
            if isDigit(T[i], T[j]):
                f[i][j] = abs(T[i] - T[j])

    toCheck = []
    for i in range(n):
        if i != minIndex and i != maxIndex:
            toCheck.append(i)

    memo(T, f, minIndex, maxIndex, n, toCheck)


T = [123,890,688,587,257,246]
minCost(T)