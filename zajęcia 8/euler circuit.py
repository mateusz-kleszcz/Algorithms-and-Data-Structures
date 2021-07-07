def Euler(G):

    n = len(G)

    cycle = [] # tej tablicy będę używał do przechowywania znalezionego cyklu Eulera

    #sprawdzam czy graf jest spójny i czy wszystkie wierzchołki mają stopień parzysty, jeżeli nie jest to od razu zwracam informację że nie ma on cyklu (złożoność O(v^2))
    for i in range(n):
        isDisconnected = True
        sum = 0
        for j in range(n):
            if G[i][j] == 1:
                isDisconnected = False
                sum += 1
        if isDisconnected or sum % 2:
            return None

    # trochę denerwowało mnie, że gdy dfs wejdzie np ponownie do wierzchołka, który został już częściowo przetworzony, to sprawdza od początku krawędzie nawet jeżeli oznaczyłem dwójką jako odwiedzone
    # wprowadzam więc licznik który sprawdza które krawędzie były już przetworzone (mój algorytm sprawdza krawędzie po kolei w wierszach)
    # nie zmienia to chyba ogólnej złożoności O(v^2) i powoduje że używam v dodatkowej pamięci ale dla np grafu pełnego o 5 wierzchołkach zmniejszyło liczbę operacji z 49 do 26
    counters = [0] * n

    def DFSVisited(u, counter):
        for v in range(counters[u], n): # zaczynam sprawdzanie od krawędzi która jeszcze nie sprawdziłem a nie od 0
            if counters[u] == n: # jeżeli przetworzyłem wszystkie krawędzie to już nie mam co sprawdzać
                break
            if v != u and G[u][v] == 1:
                G[u][v] = 2 #ustawiam krawędź jako odwiedzoną, ale nie usuwam jej
                G[v][u] = 2 #w obydwóch miejscach
                counters[u] = v + 1 # poprzednich krawędzi już nie muszę sprawdzać ponownie
                DFSVisited(v, counter + 1)
        # jeżeli przetworzyłem jakiś wierzchołek to dodaje go do cyklu
        counters[u] = n
        cycle.append(u)

    #sprawdziłem czy graf jest spójny, więc wystarczy że wywołam funkcję dfs dla jednego wierzchołka
    DFSVisited(0, 0)

    # powracam do pierwotnego wyglądu macierzy G
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                G[i][j] = 1

    return cycle


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]


print(Euler(G))
G = [[0, 1, 0, 1, 1],
     [1, 0, 1, 1, 0],
     [0, 1, 0, 1, 0],
     [1, 1, 1, 0, 0],
     [1, 0, 0, 0, 0]]
print(Euler(G))