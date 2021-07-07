def tasks(T):
    n = len(T)

    stack = []
    visited = [0] * n

    def DFSVisit(G, u):
        visited[u] = True
        for v in range(n):
            if not visited[v] and G[u][v] == 1:
                DFSVisit(G, v)
        stack.append(u)

    for u in range(n):
        if not visited[u]:
            DFSVisit(T, u)

    return stack[::-1]