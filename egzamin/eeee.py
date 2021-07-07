inf = float('inf')

def letters(G, W):
    n = len(G[0])
    T = [inf] * n

    for i in range(n):
        if G[0][i] == W[0]:
            T[i] = 0

    for j in range(len(W) - 1):
        a = W[j]
        b = W[j + 1]
        print(a, b)

        for i in range(n):
            if G[0][i] != a:
                T[i] = inf
        print(T)
        for edge in G[1]:
            if G[0][edge[0]] == a and G[0][edge[1]] == b:
                new_d = T[edge[0]] + edge[2]
                if T[edge[1]] > new_d:
                    T[edge[1]] = new_d

            elif G[0][edge[0]] == b and G[0][edge[1]] == a:
                new_d = T[edge[1]] + edge[2]
                if T[edge[0]] > new_d:
                    T[edge[0]] = new_d
        print(T)

    best = inf
    for i in range(n):
        if G[0][i] == W[len(W) - 1] and T[i] < best:
            best = T[i]

    return best


L2 = ["m","a","g","a","g","m","i","i","a"]
E2 = [(0,2,3),(0,1,1),(1,2,2),(1,4,5),(2,3,1),(3,4,4),(3,5,2),(4,6,1),(4,8,100),(4,7,3),(5,7,7),(5,8,1),(7,8,6) ]
print(letters((L2, E2), 'magia'))