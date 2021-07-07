def letters(G, W):
    L, E, = G
    n = len(L)
    p = len(W)

    E.sort(key=lambda x: x[2])

    words = [False] * (p - 1)
    MST = [[] for _ in range(n)]

    for u, v, w in E:
        isEdge = False
        for i in range(p - 1):
            if (W[i] == L[u] and W[i + 1] == L[v]) or (W[i] == L[v] and W[i + 1] == L[u]):
                words[i] = True
                isEdge = True

        if isEdge:
            MST[u].append((v, w))

        isAllWords = True
        for word in words:
            if not word:
                isAllWords = False
                break

        if isAllWords:
            break

    source = []
    for i in range(p):
        if L[i] == W[0]:
            source.append(i)

    MST.append(source)



L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
G = (L,E)
letters(G, 'kto')