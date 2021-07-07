def transitive(G):
    n = len(G)

    tc = [[0] * n for _ in range(n)]



G = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
]
print(transitive(G))