def knapsack(v, w, h, maxW, maxH):
    n = len(v)

    f = [[[0] * (maxH + 1) for _ in range(maxW + 1)] for _ in range(n)]

    for weight in range(w[0], maxW + 1):
        for height in range(h[0], maxH + 1):
            f[0][weight][height] = v[0]

    for i in range(1, n):
        for width in range(1, maxW + 1):
            for height in range(1, maxH + 1):
                f[i][width][height] = f[i - 1][width][height]
                if w[i] <= width and h[i] <= height:
                    f[i][width][height] = max(f[i][width][height], f[i - 1][width - w[i]][height - h[i]] + v[i])

    return f[n - 1][maxW][maxH]


v = [1, 2, 3, 5, 7]
w = [5, 7, 6, 3, 4]
h = [8, 9, 2, 1, 4]
knapsack(v, w, h, 13, 10)