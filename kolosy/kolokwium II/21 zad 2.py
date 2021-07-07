from queue import Queue

def BFS(G, s, t):
    n = len(G)

    visited = [False] * n
    dist = [-1] * n

    q = Queue()
    visited[s] = True
    dist[s] = 0
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                dist[v] = dist[u] + 1
                visited[v] = True
                if v == t:
                    return dist
                q.put(v)

    return dist


def enlarge(G, s, t):
    n = len(G)

    distFromStoT = BFS(G, s, t)
    distFromTtoS = BFS(G, t, s)

    length = distFromStoT[t]
    counters = [0] * (length + 1)
    # liczę ile wierzchołków będących częścią najkrótszej ścieżki jest oddalonych od s o wartość v
    for v in range(n):
        if distFromStoT[v] != -1 and distFromTtoS[v] != -1 and distFromTtoS[v] + distFromStoT[v] == length:
            counters[distFromStoT[v]] += 1

    prev = - 1
    for i in range(len(counters)):
        curr = counters[i]
        #jeżeli po sobie występują dwa wierzchołki będące częścią najkrótszej ścieżki to je trzeba usunąć
        if curr == 1 and prev == 1:
            x = -1
            y = -1
            # szukam jakie mają indeksy
            for k in range(n):
                if distFromTtoS[k] == length - i and distFromStoT[k] == i:
                    y = k
                if distFromTtoS[k] == length - i + 1 and distFromStoT[k] == i - 1:
                    x = k
            return (x, y)
        prev = curr

    return None


G = [ [1,4],  # 0
       [0,2],  # 1
       [1,3],  # 2
       [2,5],  # 3
       [0,5],  # 4
       [4,3]]  # 5
s = 0
t = 2

print(enlarge(G, s, t))