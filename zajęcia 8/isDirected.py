def isDirected(G):
    n = len(G)

    matrix = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            matrix[u][v] = 1

    for i in range(n):
        print(matrix[i])

    for i in range(n):
        for j in range(n):
            if G[i][j] != G[j][i]:
                return False

    return True


G = [
    [1, 3],
    [0, 2, 9, 10],
    [1, 3],
    [0, 2, 4],
    [3, 5, 6],
    [4],
    [4, 7],
    [8],
    [7],
    [2, 10],
    [9]
]
print(isDirected(G))