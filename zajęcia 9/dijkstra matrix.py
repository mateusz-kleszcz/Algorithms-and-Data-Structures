def dijksta(G):
    n = len(G)
    visited = [False] * n
    dist = [float('inf')] * n

    dist[0] = 0
    for i in range(n):

        minimum = float('inf')
        u = -1
        for j in range(n):
            if not visited[j] and dist[j] < minimum:
                minimum = dist[j]
                u = j

        visited[u] = True

        for v in range(n):
            if G[u][v] != -1 and not visited[v]:
                if dist[u] + G[u][v] < dist[v]:
                    dist[v] = dist[u] + G[u][v]

    return dist



G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]
print(dijksta(G))