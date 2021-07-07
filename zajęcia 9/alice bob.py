from queue import PriorityQueue

def relax(u, v, w, dist, parent, q):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = u // 2
        q.put((dist[v], v))


def alice(G, a, b):
    n = len(G)

    dist = [float('inf')] * (2 * n)
    visited = [False] * (2 * n)
    parent = [None] * (2 * n)

    dist[a * 2] = 0
    dist[a * 2 + 1] = 0
    q = PriorityQueue()
    q.put((0, a * 2))
    q.put((0, a * 2 + 1))

    while not q.empty():
        weight, u = q.get()
        visited[u] = True
        for e in range(len(G[u // 2])):
            v, w = G[u // 2][e]
            if u % 2:
                nxt = v * 2
                if not visited[nxt]:
                    relax(u, nxt, w, dist, parent, q)
            else:
                nxt = v * 2 + 1
                if not visited[nxt]:
                    relax(u, nxt, 0, dist, parent, q)

    if dist[b * 2 + 1] < dist[b * 2]:
        result = dist[b * 2 + 1]
        who = 'Alice'
        index = b * 2 + 1
        route = [b]
        i = 0
        while parent[index] != None:
            route.append(parent[index])
            index = parent[index] * 2 + i
            i = 0 if i else 1

    else:
        result = dist[b * 2]
        who = 'Bob'
        index = b * 2
        route = [b]
        i = 1
        while parent[index] != None:
            route.append(parent[index])
            index = parent[index] * 2 + i
            i = 0 if i else 1

    route.reverse()

    return result, who, route


G = [
    [(1, 4), (7, 8)],
    [(0, 4), (2, 8), (7, 11)],
    [(1, 8), (3, 7), (8, 2), (5, 4)],
    [(2, 7), (5, 14), (4, 9)],
    [(3, 9), (5, 10)],
    [(4, 10), (3, 14), (2, 4), (6, 2)],
    [(7, 1), (5, 2), (8, 6)],
    [(6, 1), (1, 11), (8, 7), (0, 8)],
    [(2, 2), (6, 6), (7, 7)]
]
print(alice(G, 0, 4))