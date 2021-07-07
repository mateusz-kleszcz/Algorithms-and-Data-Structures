def airplane(G, s, k, t):

    n = len(G)
    isPossible = False

    def DFSVisit(u, floor, ceil, visited):
        nonlocal isPossible
        for el in range(G[u]):
            v, value = el
            if not visited[v] and floor <= value <= ceil:
                if v == k:
                    isPossible = True
                    return True
                visited[v] = True
                DFSVisit(v, floor, ceil, visited)

    for el in range(G[s]):
        u, value = el
        floor = value - t
        ceil = value + t
        visited = [False for _ in range(n)]
        DFSVisit(u, floor, ceil, visited)

    return isPossible