from queue import PriorityQueue

def jak_dojade(G, P, d, a, b):
    n = len(G)
    all = (d + 1) * n
    P.sort()

    vertexes = [i % (d + 1) for i in range(all)]
    isPetrolStation = [False] * n
    for price in P:
        isPetrolStation[price] = True
        for i in range(d + 1):
            vertexes[price * (d + 1) + i] = d

    q = PriorityQueue()
    visited = [False] * all
    dist = [float('inf')] * all
    parent = [None] * all
    q.put((0, d, a))
    dist[a * (d + 1) + d] = 0
    visited[a * (d + 1) + d] = True

    while not q.empty():
        weight, fuel, u = q.get()
        curr = u * (d + 1) + fuel
        visited[curr] = True
        for v in range(n):
            cost = G[u][v]
            nxt = v * (d + 1) + fuel - cost
            if cost != -1 and fuel - cost >= 0 and not visited[nxt]:
                if dist[nxt] > dist[curr] + G[u][v]:
                    dist[nxt] = dist[curr] + G[u][v]
                    parent[nxt] = curr
                    if isPetrolStation[v]:
                        if dist[nxt] < dist[v * (d + 1) + d]:
                            dist[v * (d + 1) + d] = dist[nxt]
                            parent[v * (d + 1) + d] = parent[nxt]
                    q.put((dist[nxt], vertexes[nxt], v))

    minCost = float('inf')
    minIndex = -1
    result = [b]

    for i in range(n):
        index = b * (d + 1) + i
        if dist[index] < minCost:
            minCost = dist[index]
            minIndex = index

    if minCost == float('inf'):
        return None

    while parent[minIndex] != None:
        minIndex = parent[minIndex]
        result.append(minIndex // (d + 1))

    result.reverse()

    return result


# G = [[-1, 5, -1, 2],
#     [-1, -1, -1, -1],
#     [5, -1, -1, 5],
#     [2, 2, -1, -1]]
# P = [2, 0]
# print(jak_dojade(G, P, 6, 2, 1))