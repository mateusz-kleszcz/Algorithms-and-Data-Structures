def memo(tab, f, i, d, g, l):

    if i >= 0 and d <= l and g <= l:

        if f[i][d][g] != 0:
            return f[i][d][g]

        f[i][d][g] = memo(tab, f, i - 1, d + tab[i - 1], g, l) or memo(tab, f, i - 1, d, g + tab[i - 1], l)

        return f[i][d][g]

    return 0


def ferry(tab, l):
    n = len(tab)
    f = [[[0] * (l + 1) for _ in range(l + 1)] for _ in range(n + 1)]

    f[0][l][l] = 1

    for i in range(n):
        for g in range(l):
            for d in range(l):
                memo(tab, f, i, g, d, l)

    for i in range(1, n + 1):
        isPossible = False
        for g in range(l + 1):
            for d in range(l + 1):
                if f[i][g][d]:
                    isPossible = True
        if not isPossible:
            return i

    return n


tab = [1, 4, 3, 2, 7, 8]
l = 8
print(ferry(tab, l))