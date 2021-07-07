def letters(G, W):

    L, E = G

    d = len(W)

    dist = [[float('inf')] * len(E) for _ in range(d)]

    for i in range(len(E)):
        dist[0][i] = 0

    for i in range(d - 1):
        for j in range(len(E)):

            a, b = W[i], W[i + 1]
            u, v, w = E[j]

            if L[u] == a and L[v] == b:
                if dist[i][u] != None:
                    dist[i + 1][v] = min(dist[i + 1][v], dist[i][u] + w)

            if L[v] == a and L[u] == b:
                if dist[i][v] != None:
                    dist[i + 1][u] = min(dist[i + 1][u], dist[i][v] + w)

    result = min(dist[d - 1])

    if result == float('inf'):
        return -1

    return result