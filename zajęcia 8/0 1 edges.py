from collections import deque

def printSolution(parent, i, s):
    if i == s:
        print(s, end=' ')
    else:
        printSolution(parent, parent[i], s)
        print(i, end=' ')


def edges(G, s, k):

    n = len(G)
    minimumCost = [float('inf')] * n
    parent = [None] * n
    minimumCost[s] = 0

    q = deque()
    q.append(s)

    while q:
        u = q.popleft()
        for el in G[u]:
            v, isToll = el
            if minimumCost[v] > minimumCost[u] + isToll:
                minimumCost[v] = minimumCost[u] + isToll
                parent[v] = u
                if isToll:
                    q.appendleft(v)
                else:
                    q.append(v)

    printSolution(parent, k, s)


G = [
    [(1, 0), (7, 1)],
    [(2, 0), (5, 0)],
    [(3, 1), (4, 0)],
    [(8, 1)],
    [],
    [(6, 1)],
    [(0, 0)],
    [(3, 1)],
    [(9, 0), (10, 1)],
    [(10, 0)],
    [],
]

edges(G, 0, 10)