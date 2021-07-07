def hamilton(G):
    n = len(G)

    visited = [False] * n
    stack = []

    def DFSVisit(G, u):
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                DFSVisit(G, v)
        stack.append(u)

    DFSVisit(G, 0)

    if len(stack) != n:
        return False

    while len(stack) > 1:
        u = stack.pop()
        nxt = stack.pop()
        isPossible = False
        for v, w in G[u]:
            if v == nxt:
                isPossible = True

        if not isPossible: return False
        stack.append(nxt)

    return True


G = [
    [(1, 5), (2, 3)],
    [(3, 6), (2, 2)],
    [(4, 5), (5, 2), (3, 7)],
    [(4, -1)],
    [(5, -2)],
    []
]
print(hamilton(G))