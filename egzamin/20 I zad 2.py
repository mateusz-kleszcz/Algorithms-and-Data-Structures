# dynamik (podobny do mnożenia macierzy)
# f(i, j) - największa wartość bezwzględna która pojawiła się przy dodawaniu od i do j elementu
# rozwiązanie to f(1, k) - największa wartośc przy dodawaniu a1 + a2 + ... + ak
# f(i, j) = max{
# abs(suma(j, i)), - sumujemy po kolei wszystkie i sprawdzamy wartość bezwzględna
# min{f(i + 1, j), f(i, j - 1)} - najmniejsza z poprzednich, ją wybrałem żeby móc wykonać to dodawanie
# }
def opt_sum(tab):
    n = len(tab)

    f = [[0] * n for _ in range(n)]
    sums = [0] * (n + 1)

    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + tab[i - 1]

    for x in range(1, n):
        for i in range(n - x):
            j = x + i
            f[i][j] = abs(sums[j + 1] - sums[i])

            print(f[i][j])
            best = float('inf')
            for k in range(i, j):
                best = min(max(f[k + 1][j], f[i][k]), best)
                print(i, j, k, best)

            f[i][j] = max(f[i][j], best)

    for row in f:
        print(row)

    return f[0][n - 1]


t = [1, -5, 3, -1, -3, 5, -8, 3, 2, -7, 6, 3]
print(opt_sum(t))