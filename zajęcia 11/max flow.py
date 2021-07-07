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


graph = [[0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]]

print(fordFulkerson(graph, 0, 5))