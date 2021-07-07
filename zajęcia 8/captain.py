def captain(G, t):
    m = len(G)
    n = len(G[0])

    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    isPossible = False

    dirX = [-1, 0, 1, 0]
    dirY = [0, -1, 0, 1]

    def DFSVisit(x, y):
        nonlocal isPossible
        for i in range(4):
            nextX = x + dirX[i]
            nextY = y + dirY[i]
            if 0 <= nextX < m and 0 <= nextY < n:
                if not visited[nextX][nextY] and G[nextX][nextY] > t:
                    if nextX == m - 1 and nextY == n - 1:
                        isPossible = True
                        return True
                    visited[nextX][nextY] = True
                    DFSVisit(nextX, nextY)

    DFSVisit(0, 0)

    return isPossible


G = [[8, 9, 10, 12],
     [5, 6, 5, 7],
     [4, 1, 12, 13]]
print(captain(G, 7))