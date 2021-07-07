from queue import Queue

def BFS(G, s, k):
    n = len(G)
    q = Queue()
    visited = [False] * n
    parent = [None] * n
    d = [None] * n
    q.put(s)
    visited[s] = True
    d[s] = 0

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                q.put(v)

            if v == k:
                break

    path = [k]
    while k != s:
        path.append(parent[k])
        k = parent[k]

    return path[::-1]


g = [
    [1, 3],
    [0, 2],
    [1, 4, 3],
    [0, 2],
    [2]
]
print(BFS(g, 1, 4))