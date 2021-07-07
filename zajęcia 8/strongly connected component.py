def DFS(G):

    n = len(G)
    visited = [False for _ in range(n)]
    stack = []

    def DFSVisit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)
        stack.append(u)

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    Greverse = [[] for _ in range(n)]
    for i in range(n):
        for el in G[i]:
            Greverse[el].append(i)

    visited = [False] * n
    print(stack, Greverse)

    def DFSUtil(G, u):
        visited[u] = True
        print(u, end=' ')
        for v in G[u]:
            if not visited[v]:
                DFSUtil(G, v)

    while stack:
        u = stack.pop()
        if not visited[u]:
            DFSUtil(Greverse, u)
            print('')


G = [[1],
     [2, 3],
     [0],
     [4],
     [5],
     [3]]
DFS(G)