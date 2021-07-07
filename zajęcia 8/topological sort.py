def topologicalSort(G):

    n = len(G)
    stack = []
    visited = [False] * n

    def DFSVisit(G, u):
        visited[u] = True
        for v in range(n):
            if not visited[v] and G[u][v]:
                DFSVisit(G, v)
        stack.append(u)


    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    print(stack[::-1])


G = [[0, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 1, 0, 1],
     [0, 1, 1, 0]]

print(topologicalSort(G))