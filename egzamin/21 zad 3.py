from zad3testy import runtests

def jumper(G, s, w):
    n = len(G)

    twoMilesG = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] > 0:
                for k in range(n):
                    if G[j][k] > 0:
                        if twoMilesG[i][k] > max(G[i][j], G[j][k]):
                            twoMilesG[i][k] = max(G[i][j], G[j][k])
    for i in range(n):
        twoMilesG[i][i] = 0
        print(twoMilesG[i])
    dist = [float('inf')] * (2 * n)
    dist[s] = 0
    dist[s + n] = 0
    visited = [False] * (2 * n)

    for i in range(2 * n):

        u = -1
        minimum = float('inf')
        for j in range(2 * n):
            if not visited[j] and minimum > dist[j]:
                u = j
                minimum = dist[j]

        visited[u] = True

        for v in range(n):
            weight = G[u % n][v]
            if u < n:
                if not visited[v + n] and twoMilesG[u][v] > 0:
                    if dist[v + n] > dist[u] + twoMilesG[u][v]:
                        dist[v + n] = dist[u] + twoMilesG[u][v]
            if not visited[v] and G[u % n][v] > 0:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight

    return min(dist[w], dist[w + n])


runtests(jumper)