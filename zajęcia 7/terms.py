def terms(d, g):
    n = len(d)

    t = [0] * n
    for i in range(n):
        t[i] = (d[i], g[i])
    t.sort()

    maximum = t[n - 1][1]
    cost = 0
    for i in range(n - 2, -1, -1):
        if t[i][0] != t[i + 1][0]:
            cost += maximum
            maximum = t[i][1]
        elif t[i][1] > maximum:
            maximum = t[i][1]

    cost += maximum

    return cost


d = [2, 1, 3, 4, 3, 1, 1, 2]
g = [7, 5, 4, 3, 2, 4, 4, 1]
print(terms(d, g))