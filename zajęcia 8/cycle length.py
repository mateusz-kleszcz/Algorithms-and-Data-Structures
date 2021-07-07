def cycle(G):
    n = len(G)

    c = [-1] * n
    d = [0] * n

    for u in range(n):
        c[u] = 0
        for v in range(n):
            if u != v and G[u][v]:
                c[v] = 1
                for k in range(n):
                    if k != u and k != v and G[v][k]:
                        d[k] += 1
                        if d[k] == 2:
                            for i in range(n):
                                if c[i] == 1 and i != v and i != k:
                                    if G[u][i] and G[i][k]:
                                        return u, v, k, i
        c = [-1] * n
        d = [0] * n

    return False


G = [[0, 1, 1, 1, 1],
     [1, 0, 1, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 1, 0, 1],
     [1, 1, 1, 1, 0]]

print(cycle(G))