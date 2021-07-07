from queue import PriorityQueue

def prim(G):
    n = len(G)

    visited = [False] * n
    parent = [None] * n
    key = [float('inf')] * n

    q = PriorityQueue()
    key[0] = 0
    q.put((0, 0))

    while not q.empty():
        weight, u = q.get()
        visited[u] = True
        for e in range(len(G[u])):
            v, w = G[u][e]
            if not visited[v]:
                if w < key[v]:
                    key[v] = w
                    parent[v] = u
                    q.put((w, v))

    spanningTree = [[] for _ in range(n)]
    minCost = 0
    for u in range(1, n):
        v = parent[u]
        spanningTree[v].append(u)
        spanningTree[u].append(v)
        minCost += key[u]

    return spanningTree, minCost


G = [
    [(1, 4), (7, 8)],
    [(0, 4), (2, 8), (7, 11)],
    [(1, 8), (3, 7), (8, 2), (5, 4)],
    [(2, 7), (5, 14), (4, 9)],
    [(3, 9), (5, 10)],
    [(4, 10), (3, 14), (2, 4), (6, 2)],
    [(7, 1), (5, 2), (8, 6)],
    [(6, 1), (1, 11), (8, 7), (0, 8)],
    [(2, 2), (6, 6), (7, 7)]
]
prim(G)