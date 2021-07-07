from queue import Queue

def islands (G, s, t):

    n = len(G)

    # rozmnożenie wierzchołków
    dist = [float('inf')] * (3 * n)
    visited = [False] * (3 * n)

    q = Queue()
    # do wierzchołków startowych w pierwszym wykonaniu kolejki dodam wartości tak aby były równe 0 po wykonaniu pierwszych 3 iteracji
    dist[s * 3] = -1
    dist[s * 3 + 1] = -5
    dist[s * 3 + 2] = -8
    # do kolejki dodaję krotkę postaci (wierzchołek do którego idę, ile drogi mi zostało do niego, wierzchołek z którego idę)
    q.put((s * 3, 0, s * 3))
    q.put((s * 3 + 1, 0, s * 3 + 1))
    q.put((s * 3 + 2, 0, s * 3 + 2))

    while not q.empty():
        u, value, parent = q.get()

        # jeżeli jeszcze nie dotarłem to w tym momencie przechodzę o 1 jednostkę
        if value > 0:
            q.put((u, value - 1, parent))
            continue

        # jeżeli wierzchołek do którego dotarłem był już wcześniej odwiedzony to pomijam
        if visited[u]: continue

        visited[u] = True
        state = u % 3
        # stan 0 oznacza że przyszedłem mostem
        # stan 1 oznacza że przyszedłem promem
        # stan 2 oznacza że przyszedłem przelotem
        if state == 0:
            dist[u] = dist[parent] + 1
        if state == 1:
            dist[u] = dist[parent] + 5
        if state == 2:
            dist[u] = dist[parent] + 8

        for v in range(n):
            if G[u // 3][v] > 0:
                # dla każdej istniejącej krawędzi sprawdzam czy nie jest tym samym środkiem transportu z którego przyszedłem
                # i czy wierzchołek do którego chce dotrzeć nie jest już odwiedzony
                # jak nie to dodaję go do kolejki
                if G[u // 3][v] == 1 and state != 0 and not visited[v * 3]:
                    q.put((v * 3, 1, u))
                if G[u // 3][v] == 5 and state != 1 and not visited[v * 3 + 1]:
                    q.put((v * 3 + 1, 5, u))
                if G[u // 3][v] == 8 and state != 2 and not visited[v * 3 + 2]:
                    q.put((v * 3 + 2, 8, u))

    # wynik to najniższy koszt dotarcia do wierzchołka t za pomocą mostu, promu lub przelotu
    return min(dist[t * 3], dist[t * 3 + 1], dist[t * 3 + 2])


G1 = [ [0,5,1,8,0,0,0 ],
       [5,0,0,1,0,8,0 ],
       [1,0,0,8,0,0,8 ],
       [8,1,8,0,5,0,1 ],
       [0,0,0,5,0,1,0 ],
       [0,8,0,0,1,0,5 ],
       [0,0,8,1,0,5,0 ] ]

print(islands(G1, 5, 2))