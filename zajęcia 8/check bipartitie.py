import queue

def check(G):
    n = len(G)
    q = queue.Queue()

    colors = [-1] * n

    for i in range(n):
        if colors[i] == -1:
            q.put(i)
            colors[i] = 0
            while not q.empty():
                u = q.get()
                for v in G[u]:
                    if colors[v] == colors[u]:
                        return False
                    if colors[v] == -1:
                        colors[v] = 0 if colors[u] else 1
                        q.put(v)

    return True



G = [[1], [0, 2], [1], [0, 2]]
print(check(G))