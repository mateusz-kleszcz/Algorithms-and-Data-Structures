def transitive(G):
    n = len(G)

    reachable = [[0] * n for _ in range(n)]

    for v in range(n):
        for u in range(n):
            if G[v][u] != 0:
                reachable[v][u] = 1
        reachable[v][v] = 1

    for t in range(n):
        for u in range(n):
            for w in range(n):
                reachable[u][w] = reachable[u][w] or (reachable[u][t] and reachable[t][w])

    for i in range(n):
        reachable[i][i] = 0

    return reachable


G = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
]
print(transitive(G))