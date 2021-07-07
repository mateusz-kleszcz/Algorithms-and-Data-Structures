def shortest(G, a, b):
    n = len(G)

    dist = [float('inf')] * n
    visited = [False] * n
    stack = []

    def DFSVisit(G, u):
        visited[u] = True
        for e in G[u]:
            v, w = e
            if not visited[v]:
                DFSVisit(G, v)
        stack.append(u)

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    dist[a] = 0

    while stack:
        i = stack.pop()
        for u, w in G[i]:
            if dist[u] > dist[i] + w:
                dist[u] = dist[i] + w

    return dist[b]


G = [
    [(1, 5), (2, 3)],
    [(3, 6), (2, 2)],
    [(4, 5), (5, 2), (3, 7)],
    [(4, -1)],
    [(5, -2)],
    []
]
print(shortest(G, 1, 4))