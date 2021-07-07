from queue import Queue

def BFS(G, s, t, parent):
    n = len(G)

    q = Queue()
    visited = [False] * n

    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()
        for v, value in G[u]:
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
            for v in range(len(G[parent[sink]])):
                index, flow = G[parent[sink]][v]
                if index == sink and flow < pathFlow:
                    pathFlow = flow
            sink = parent[sink]

        maxFlow += pathFlow

        v = t
        while v != s:
            u = parent[v]
            for i in range(len(G[u])):
                index, value = G[u][i]
                if index == v:
                    G[u][i] = (v, value - 1)
            for i in range(len(G[v])):
                index, value = G[v][i]
                if index == u:
                    G[v][i] = (u, value + 1)
            v = parent[v]

    return maxFlow


def matching(G):
    n = len(G)

    superSource = []
    superSink = []

    q = Queue()
    visited = [False] * n
    superSource.append(0)
    q.put((0, 0))

    while not q.empty():
        u, dist = q.get()
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                if dist % 2 == 0:
                    superSink.append(v)
                else:
                    superSource.append(v)
                q.put((v, dist + 1))

    newG = [[] for _ in range(n + 2)]

    for s in superSource:
        for e in G[s]:
            newG[s].append((e, 1))
        newG[s].append((n, 0))
        newG[n].append((s, 1))

    for t in superSink:
        for e in G[t]:
            newG[t].append((e, 0))
        newG[t].append((n + 1, 1))
        newG[n + 1].append((t, 0))

    return fordFulkerson(newG, n, n + 1)


G = [
    [2, 4],
    [3],
    [0],
    [1, 4],
    [0, 3]
]
print(matching(G))