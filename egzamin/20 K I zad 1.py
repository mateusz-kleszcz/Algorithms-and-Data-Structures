def jak_dojade(G, P, d, a, b):
    n = len(G)
    vertexNum = (d + 1) * n

    visited = [False] * vertexNum
    parent = [-1] * vertexNum
    dist = [float('inf')] * vertexNum

    petrolStation = [False] * n
    for p in P:
        petrolStation[p] = True
    petrolStation[a] = True

    dist[a * (d + 1) + d] = 0

    for i in range(vertexNum):

        u = -1
        minimum = float('inf')
        for j in range(vertexNum):
            if not visited[j] and minimum > dist[j]:
                u = j
                minimum = dist[j]

        visited[u] = True

        petrolInU = u % (d + 1)

        for v in range(n):
            weight = G[u // (d + 1)][v]
            index = v * (d + 1) + petrolInU - weight
            if petrolStation[v]: index = v * (d + 1) + d
            if weight != -1 and weight <= petrolInU and not visited[index]:
                if dist[index] > dist[u] + weight:
                    dist[index] = dist[u] + weight
                    parent[index] = u

    t = -1
    minDist = float('inf')
    for i in range(b * (d + 1), b * (d + 1) + d):
        if dist[i] < minDist:
            minDist = dist[i]
            t = i

    if minDist == float('inf'):
        return None

    path = []

    while t != -1:
        path.append(t // (d + 1))
        t = parent[t]

    return path[::-1]