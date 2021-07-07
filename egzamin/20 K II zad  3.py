def dijksta(G, s, t):
    n = len(G)
    visited = [False] * n
    dist = [float('inf')] * n

    dist[s] = 0
    for i in range(n):

        minimum = float('inf')
        u = -1
        for j in range(n):
            if not visited[j] and dist[j] < minimum:
                minimum = dist[j]
                u = j

        visited[u] = True

        for v in range(n):
            if G[u][v] != -1 and not visited[v]:
                if dist[u] + G[u][v] < dist[v]:
                    dist[v] = dist[u] + G[u][v]

    return dist[t]


def isSameDigit(a, b):
    result = abs(a - b)
    digitA = [0] * 10
    digitB = [0] * 10
    while a >= 1:
        digitA[a % 10] += 1
        a //= 10
    while b >= 1:
        digitB[b % 10] += 1
        b //= 10

    for i in range(10):
        if digitA[i] > 0 and digitB[i] > 0:
            return result
    return -1


def shortest(T):
    n = len(T)

    G = [[float('inf')] * n for _ in range(n)]
    T.sort()

    for i in range(n):
        for j in range(n):
            value = isSameDigit(T[i], T[j])
            if value != -1:
                G[i][j] = value

    result = dijksta(G, 0, n - 1)

    if result == float('inf'):
        return -1

    return result