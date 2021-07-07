def floyd(G):
    n = len(G)

    dist = [[float('inf')] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    for v in range(n):
        for u in range(n):
            if G[v][u] != float('inf'):
                dist[v][u] = G[v][u]
                parent[v][u] = v
        dist[v][v] = 0

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if dist[u][t] + dist[t][w] < dist[u][w]:
                    dist[u][w] = dist[u][t] + dist[t][w]
                    parent[u][w] = parent[t][w]

    return dist


G = [
    [0, 3, 8, float('inf'), -4],
    [float('inf'), 0, float('inf'), 1, 7],
    [float('inf'), 4, 0, float('inf'), float('inf')],
    [2, float('inf'), -5, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0],
]
floyd(G)