from math import ceil

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


def highway(A):
    n = len(A)

    edges = []

    for i in range(n):
        for j in range(i, n):
            if i != j:
                x1, y1 = A[i]
                x2, y2 = A[j]
                time = ceil(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                edges.append((i, j, time))

    edges.sort(key=lambda x: x[2])

    minDifference = float('inf')

    for i in range(len(edges)):

        subsets = [Node(v) for v in range(n)]

        minimum = float('inf')
        maximum = -1
        length = 0

        for j in range(i, len(edges)):
            u, v, w = edges[j]

            x = find(subsets[u])
            y = find(subsets[v])

            if x != y:
                union(x, y)
                length += 1
                if minimum > w:
                    minimum = w
                if maximum < w:
                    maximum = w

        if length + 1 == n:
            minDifference = min(minDifference, maximum - minimum)

    return minDifference