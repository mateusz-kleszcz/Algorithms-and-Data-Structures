def tanagram(x, y, t):
    n = len(x)

    countersX = [[] for _ in range(26)]
    countersY = [[] for _ in range(26)]
    for i in range(n):
        charX = x[i]
        countersX[ord(charX) - 97].append(i)
        charY = y[i]
        countersY[ord(charY) - 97].append(i)

    for i in range(26):
        X = countersX[i]
        Y = countersY[i]
        m = len(X)
        for j in range(m):
            if not X[j] - t <= Y[j] <= X[j] + t:
                return False

    return True


tanagram('egzamin', 'gezamin', 3)