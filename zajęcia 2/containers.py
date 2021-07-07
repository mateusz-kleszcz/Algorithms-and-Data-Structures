def containters(T, v):
    n = len(T)

    #policzenie wszystkich objętości i znalezienie najmniejszej z nich
    minV = 99999999
    sumV = 0
    for i in range(n):
        x1, y1 = T[i][0]
        x2, y2 = T[i][1]
        v = (x2 - x1) * (y1 - y2)
        if minV > v: minV = v
        sumV += v

    #znalezienie najniższej podstawy pojemnika i najwyższej góry pojemnika
    #oraz wyznaczenie środka
    maxY = T[0][0][1]
    minY = T[0][1][1]
    for container in T:
        y1 = container[0][1]
        y2 = container[1][1]
        if maxY < y1:
            maxY = y1
        if minY > y2:
            minY = y2
    mid = (minY + maxY) / 2

    while sumV - minV > v:
        sumV = 0
        for container in T:
            x1, y1 = container[0]
            x2, y2 = container[1]
            if y2 > mid: continue
            v = (x2 - x1) * min(mid - y2, y1 - y2)
            sumV += v
        mid /= 2

    counter = 0
    for container in T:
        y1 = container[0][0]
        if y1 < mid: counter += 1
    return T


tab = [[(1, 2), (2, 0)], [(3, 7), (4, 1)], [(5, 6), (12, 4)]]
a = 10
print(containters(tab, a))