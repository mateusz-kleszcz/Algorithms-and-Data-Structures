def printSolution(parent, i, s):
    if i == s:
        print(s, end=' ')
    else:
        printSolution(parent, parent[i], s)
        print(i, end=' ')


def decreasing(G, s, k):
    n = len(G)

    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    isPath = False

    def DFSVisit(u, parentWeight):
        nonlocal isPath
        for el in G[u]:
            v, weight = el
            visited[u] = True
            if not visited[v] and parentWeight > weight:
                parent[v] = u
                if v == k:
                    isPath = True
                    return True
                DFSVisit(v, weight)

    DFSVisit(s, float('inf'))

    if isPath:
        printSolution(parent, k, s)
        return True

    return False


G = [
    [(1, 10), (6, 5), (7, 8)],
    [(0, 10), (2, 9), (5, 7)],
    [(1, 9), (3, 11), (4, 1)],
    [(2, 11), (7, 4), (8, 3)],
    [(2, 1), (5, 2)],
    [(1, 7), (4, 2), (6, 6)],
    [(0, 5), (5, 6)],
    [(3, 4)],
    [(3, 3), (9, 12), (10, 0)],
    [(8, 12), (10, 18)],
    [(8, 0), (9, 12)],
]
print(decreasing(G, 0, 10))