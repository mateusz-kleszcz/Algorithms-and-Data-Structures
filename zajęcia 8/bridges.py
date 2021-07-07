def bridges(G):

    n = len(G)
    visited = [False] * n
    parent = [None] * n
    entry = [-1] * n
    low = [-1] * n
    time = 0

    def DFSVisit(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        entry[u] = time
        low[u] = time
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v)
                low[u] = min(low[u], low[v])
            elif v != parent[u]:
                low[u] = min(low[u], entry[v])

    DFSVisit(G, 0)

    for v in range(n):
        if entry[v] == low[v] and parent[v] != None:
            print(v, parent[v])


G1 = [
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2, 4, 5],
    [3, 5],
    [3, 4],
]
bridges(G1)