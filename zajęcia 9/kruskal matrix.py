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
        for j in range(i + 1, n):
            if G[i][j] != -1:
                edges.append((G[i][j], i, j))

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


G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]
print(kruskal(G))