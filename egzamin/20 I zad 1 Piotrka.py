from collections import deque

NOTYET = 0
PROCESSING = 1
PROCESSED = 2

class vertex:
    def __init__(self, v):
        self.v = v
        self.visited = NOTYET
        self.d = float('inf')
        self.vsize = None


def islands(G, a, b):
    n = len(G)

    vertexes = [vertex(i // 3) for i in range(3 * n)]
    q = deque()

    for i in range(n):
        vertexes[3 * i].vsize = 1
        vertexes[3 * i + 1].vsize = 5
        vertexes[3 * i + 2].vsize = 8

    vertexes[a * 3].d = 0
    vertexes[a * 3].visited = PROCESSED
    q.append(vertexes[a * 3])

    while q:
        u = q.popleft()

        if u.visited == PROCESSING:
            u.d += 1
            u.vsize -= 1
            if u.vsize == 0:
                u.visited = PROCESSED
            q.append(u)
        else:
            for v in range(n):
                tmp = -1
                if G[u.v][v] == 1:
                    tmp = 0
                elif G[u.v][v] == 5:
                    tmp = 1
                elif G[u.v][v] == 8:
                    tmp = 2

                if tmp != -1 and vertexes[v * 3 + tmp].visited == NOTYET:

                    if tmp == 0:
                        vertexes[v * 3 + tmp].visited = PROCESSED
                        vertexes[v * 3 + tmp].d = u.d + 1
                    else:
                        vertexes[v * 3 + tmp].visited = PROCESSING
                        vertexes[v * 3 + tmp].d = u.d + 1
                        vertexes[v * 3 + tmp].vsize -= 1

                    q.append(vertexes[v * 3 + tmp])

    tmp = min(vertexes[b * 3].d, vertexes[b * 3 + 1].d, vertexes[b * 3 + 2].d)

    if tmp == float('inf'):
        return None

    return tmp


G1 = [ [0,5,1,8,0,0,0 ],
       [5,0,0,1,0,8,0 ],
       [1,0,0,8,0,0,8 ],
       [8,1,8,0,5,0,1 ],
       [0,0,0,5,0,1,0 ],
       [0,8,0,0,1,0,5 ],
       [0,0,8,1,0,5,0 ] ]

print(islands(G1, 5, 2))