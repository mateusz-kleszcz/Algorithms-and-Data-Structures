import queue

def letters(G, W):
    L = G[0]
    E = G[1]
    n = len(W)

    minCost = [0] * len(E)
    startIndexes = []
    q = queue.Queue()

    for i in range(n):
        if L[i] == W[0]:
            startIndexes.append(i)

    counter = 1
    for u in startIndexes:
        for v in range(len(E)):
            if u != v and E[v][0] == u and L[E[v][1]] == counter:
                print(u, v)


L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
G = (L,E)
W = 'kto'
letters(G, W)