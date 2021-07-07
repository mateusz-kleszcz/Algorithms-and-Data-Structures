def DFS(G):

    def DFSVisit(G, visited, parent, u):
        nonlocal time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, visited, parent, v)

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, visited, parent, u)

    return parent


def findCycle(G, u, prev, visited, stack):
    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            stack.append(v)
            isFound, x = findCycle(G, v, u, visited, stack)
            if isFound:
                return True, x
        elif prev != v:
            return True, v

    return False


def DFSVisit(G, u, visited):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFSVisit(G, v, visited)


def logic(arr):
    n = len(arr)

    G = [[] for _ in range(n)]
    counters = [[] * 2 for _ in range(n)]
    for u in range(n):
        for e in range(len(arr[u])):
            counters[arr[u][e][0]].append(u)

    for i in range(n):
        u, v = counters[i]
        G[u].append(v)
        G[v].append(u)

    visited = [False] * n
    stack = [4]
    cycle = []
    isCycle, u = findCycle(G, 4, 4, visited, stack)
    if not isCycle:
        return False

    v = stack.pop()
    while v != u:
        cycle.append(v)
        v = stack.pop()
    cycle.append(u)

    visited = [False] * n
    for v in cycle:
        visited[v] = True

    for u in cycle:
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v, visited)

    for v in visited:
        if not v:
            return False

    return True


arr = [
    [(0, True), (1, True), (2, True)],
    [(1, False), (3, True)],
    [(2, False), (4, True)],
    [(0, False), (3, False)],
    [(4, False)]
]
print(logic(arr))