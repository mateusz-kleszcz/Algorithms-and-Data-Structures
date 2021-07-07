from queue import Queue

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


def BFS(G, s, t):
    n = len(G)
    parent = [-1] * n
    visited = [False] * n

    q = Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in range(n):
            if not visited[v] and G[u][v]:
                visited[v] = True
                parent[v] = u
                if v == t:
                    return parent
                q.put(v)

    return parent


def keep_distance(M, x, y, d):
    n = len(M)

    dist = floyd(M)
    G = [[0] * (n ** 2) for _ in range(n ** 2)]

    # z (i, j) do (a, b)
    for i in range(n):
        for j in range(n):
            for a in range(n):
                for b in range(n):
                    if dist[a][b] >= d and (M[i][a] or i == a) and (M[j][b] or j == b) and (i != b or j != a):
                        newIndexX = i * n + j
                        newIndexY = a * n + b
                        G[newIndexX][newIndexY] = 1

    start = y * n + x
    end = x * n + y
    parent = BFS(G, start, end)

    path = []
    while end != -1:
        path.append(end)
        end = parent[end]

    for i in range(len(path)):
        ui = path[i] // n
        vi = path[i] % n
        path[i] = (ui, vi)

    return path

# M = [
#     [0, 5, 1, 0, 0, 0],
#     [5, 0, 0, 5, 0, 0],
#     [1, 0, 0, 1, 0, 0],
#     [0, 5, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, 0],
# ]
#
# x = 0
# y =  5
# d =  4
# keep_distance(M, x, y, d)
runtests(keep_distance)