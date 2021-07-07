def DFS(G):

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    process = [0 for _ in range(n)]

    def DFSVisit(u):
        nonlocal time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(v)
        process[time] = u
        time += 1

    time = 0
    DFSVisit(0)
    return process


G = [
    [1, 3],
    [0, 2, 9, 10],
    [1, 3],
    [0, 2, 4],
    [3, 5, 6],
    [4],
    [4, 7],
    [8],
    [7],
    [2, 10],
    [9]
]
print(DFS(G))