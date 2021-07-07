import queue

def BFS(G, u):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    dist = [0] * n

    q = queue.Queue()
    q.put(u)
    visited[u] = True

    maxValue = 0
    maxVertexes = u

    while not q.empty():
        u = q.get()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + 1
                if dist[v] > maxValue:
                    maxValue = dist[v]
                    maxVertexes = v
                q.put(v)

    return maxVertexes, dist[maxVertexes] + 1, parent


def best_root(L):
    end, _, _ = BFS(L, 0)
    start, length, parent = BFS(L, end)

    counter = 0
    best = start
    while counter < (length - 1) // 2:
        best = parent[best]
        counter += 1

    return best
    

L = [ [ 2 ],
    [ 2 ],
    [ 0, 1, 3],
    [ 2, 4 ],
    [ 3, 5, 6 ],
    [ 4 ],
    [ 4 ] ]