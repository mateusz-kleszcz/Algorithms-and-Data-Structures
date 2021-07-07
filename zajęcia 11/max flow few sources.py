from queue import Queue


def BFS(G, s, t, parent):
    n = len(G)

    q = Queue()
    visited = [False] * n

    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()
        for v in range(n):
            value = G[u][v]
            if not visited[v] and value > 0:
                visited[v] = True
                parent[v] = u
                q.put(v)

    return visited[t]


def fordFulkerson(G, s, t):
    n = len(G)
    parent = [-1] * n
    maxFlow = 0

    while BFS(G, s, t, parent):

        pathFlow = float('inf')
        sink = t

        while sink != s:
            pathFlow = min(pathFlow, G[parent[sink]][sink])
            sink = parent[sink]

        maxFlow += pathFlow

        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= pathFlow
            G[v][u] += pathFlow
            v = parent[v]

    return maxFlow


def fewSources(G, s, t):
    n = len(G)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += G[i][j]

    newG = [[0] * (n + 2) for _ in range(n + 2)]
    for source in s:
        newG[0][source] = sum

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            newG[i][j] = G[i - 1][j - 1]

    for sink in t:
        newG[sink + 1][n + 1] = sum

    for i in range(n + 2):
        print(newG[i])

    return fordFulkerson(newG, 0, n + 1)


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

print(fewSources(graph, [0, 3], [4, 5]))