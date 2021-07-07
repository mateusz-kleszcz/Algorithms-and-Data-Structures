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


def kruskal(G):
    n = len(G)

    edges = []
    for i in range(n):
        for j in range(len(G[i])):
            if i < G[i][j][0]:
                edges.append((G[i][j][1], i, G[i][j][0]))

    edges.sort(key=lambda x: x[0])

    result = []
    subsets = [Node(v) for v in range(n)]

    i = 0
    e = 0
    minCost = 0

    while e < n - 1:

        w, u, v = edges[i]
        i += 1

        x = find(subsets[u])
        y = find(subsets[v])

        if x != y:
            e += 1
            union(x, y)
            result.append((w, u, v))
            minCost += w

    spanningTree = [[] for _ in range(n)]

    for edge in result:
        w, u, v = edge
        spanningTree[u].append((v, w))
        spanningTree[v].append((u, w))

    return minCost, result, spanningTree


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
print(kruskal(G))