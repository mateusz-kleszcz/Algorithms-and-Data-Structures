from queue import PriorityQueue

def relax(u, v, w, dist, parent, q):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = u
        q.put((dist[v], v))


def dijkstra(G):
    n = len(G)

    visited = [False] * n
    parent = [None] * n
    dist = [float('inf')] * n

    q = PriorityQueue()
    dist[0] = 0
    q.put((0, 0))

    while not q.empty():
        weight, u = q.get()
        visited[u] = True
        for e in range(len(G[u])):
            v, w = G[u][e]
            if not visited[v]:
                relax(u, v, w, dist, parent, q)

    return dist, parent


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
print(dijkstra(G))