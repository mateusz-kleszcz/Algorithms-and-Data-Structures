def bellmanFord(G, s, t):
    n = len(G)

    dist = [float('inf')] * n
    parent = [-1] * n

    dist[s] = 0
    for i in range(1, n - 1):
        for u in range(n):
            for v in range(n):
                weight = G[u][v]
                if weight != 0 and dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    parent[v] = u

    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                if not dist[v] <= dist[u] + G[u][v]:
                    return False