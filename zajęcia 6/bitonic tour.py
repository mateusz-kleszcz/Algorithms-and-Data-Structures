C = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]
C.sort(key=lambda x:x[1])
n = len(C)

def getDistances(C):
    n = len(C)
    D = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            distance = ((C[j][1] - C[i][1]) ** 2 + (C[j][2] - C[i][2]) ** 2) ** 0.5
            D[i][j] = distance

    return D


D = getDistances(C)
F = [[float('inf')] * n for _ in range(n)]
F[0][1] = D[0][1]

def tspf(i, j, F, D):
    if F[i][j] != float('inf'):
        return F[i][j]

    if i == j - 1:
        best = float('inf')
        for k in range(j - 1):
            best = min(best, tspf(k, j - 1, F, D) + D[k][j])
        F[j - 1][j] = best
    else:
        F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]

    return F[i][j]


ans = float('inf')
index = -1
for i in range(n - 1):
    F[i][n - 1] = tspf(i, n - 1, F, D) + D[i][n - 1]
    if F[i][n - 1] < ans:
        ans = F[i][n - 1]
        index = i

print(ans)

I = [0] * n
I[0] = n - 1
I[1] = index
J = [0] * n
counterI = 2
counterJ = 0
for i in range(n - 2, index, -1):
    J[counterJ] = i
    counterJ += 1

def getReturnPath(i, j, F, I, J, isUpper, counterI, counterJ):
    if i == 0:
        return
    best = float('inf')
    minIndex = -1
    for k in range(j - 1):
        new = F[k][j - 1] + D[k][j]
        if new < best:
            best = new
            minIndex = k
    if isUpper:
        I[counterI] = minIndex
        counterI += 1
        for k in range(j - 2, minIndex, -1):
            J[counterJ] = k
            counterJ += 1
        isUpper = False
    else:
        J[counterJ] = minIndex
        counterJ += 1
        for k in range(j - 2, minIndex, -1):
            I[counterI] = k
            counterI += 1
        isUpper = True

    getReturnPath(minIndex, minIndex + 1, F, I, J, isUpper, counterI, counterJ)

getReturnPath(index, index + 1, F, I, J, False, counterI, counterJ)
print(C)
print(I, J)
print(C[0][0], end=', ')
for i in range(len(I) - 1, -1, -1):
    if I[i] != 0:
        print(C[I[i]][0], end=', ')
for i in range(len(J)):
    if J[i] != 0:
        print(C[J[i]][0], end=', ')
print(C[0][0])