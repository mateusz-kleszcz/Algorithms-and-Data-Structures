def DFS(G):

    def DFSVisit(G, visited, parent, u):
        nonlocal time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, visited, parent, v)

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, visited, parent, u)

    return parent


G = [[1, 2], [2, 4], [5], [4], [3, 5], [6], [7], []]
DFS(G)