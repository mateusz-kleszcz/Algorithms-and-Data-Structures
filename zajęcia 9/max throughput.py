class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank: y.rank + 1


def maximum(G, a, b):
    n = len(G)

    edges = []

    for u in range(n):
        for e in G[u]:
            v, w = e
            if u < v:
                edges.append((w, u, v))

    edges.sort(key=lambda x: x[0], reverse=True)
    subsets = [Node(v) for v in range(n)]

    path, y = find(subsets[edges[0][1]]), find(subsets[edges[0][2]])
    union(path, y)

    i = 1

    pathA = find(subsets[a])
    pathB = find(subsets[b])

    while k != l:
        w, u, v = edges[i]
        i += 1

        x = find(subsets[u])
        y = find(subsets[v])
        union(x, y)

        union(path, x)

        k = find(subsets[a])
        l = find(subsets[b])

        print(k.parent.val, l.parent.val)

    print(edges, i)

    return edges[i][0]


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
print(maximum(G, 0, 4))