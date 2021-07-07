from zad3EK import edmonds_karp

def floyd(G):
    n = len(G)

    dist = [[float('inf')] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    for v in range(n):
        for u in range(n):
            if G[v][u] != 0:
                dist[v][u] = G[v][u]
                parent[v][u] = v
        dist[v][v] = float('inf')

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if dist[u][t] + dist[t][w] < dist[u][w]:
                    dist[u][w] = dist[u][t] + dist[t][w]
                    parent[u][w] = parent[t][w]

    for i in range(n):
        dist[i][i] = 0

    return dist


def BlueAndGreen(T, K, D):
    n = len(T)

    dist = floyd(T)

    source = [0] * (n + 2)
    G = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        if K[i] == 'B':
            source[i] = 1
        else:
            G[i][n + 1] = 1

    G[n] = source

    for i in range(n):
        for j in range(n):
            if dist[i][j] >= D:
                G[i][j] = 1

    return edmonds_karp(G, n, n + 1)


T = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
K = ['B', 'B', 'G', 'G', 'B']
D = 2
print(BlueAndGreen(T, K, D))