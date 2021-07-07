def shortest(G, s, t):
    n = len(G)

    edges = []
    for u in range(n):
        for v, w in G[u]:
            if u < v:
                edges.append((w, u, v))

    edges.sort(reverse=True)

    dist = [float('inf')] * n
    parent = [None] * n
    dist[s] = 0

    for edge in edges:
        w, u, v = edge
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parent[v] = u
        elif dist[u] > dist[v] + w:
            dist[u] = dist[v] + w
            parent[u] = v

    result = [t]
    while parent[t] != None:
        result.append(parent[t])
        t = parent[t]

    return result[::-1]


G = [
    [(1, 9)],
    [(0, 9), (2, 10), (6, 8)],
    [(1, 10), (3, 4)],
    [(2, 4), (4, 5)],
    [(3, 5), (5, 6)],
    [(4, 6), (6, 7)],
    [(1, 8), (5, 7)],
]
print(shortest(G, 0, 2))