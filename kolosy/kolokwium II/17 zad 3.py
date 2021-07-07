def find(tab, k):
    n = len(tab)

    # gdybym miał posortować ręcznie to najpierw sortuje po y a potem stabilnie po x
    tab.sort()

    minimum = float('inf')
    for i in range(n):
        a1 = tab[i][0]
        b1 = tab[i][1]
        counter = 1
        for j in range(i, n):
            a2 = tab[j][0]
            b2 = tab[j][1]
            if a2 >= b1:
                counter += 1
                if counter == k:
                    if minimum > b2 - a1:
                        minimum = b2 - a1
                    break
                a1 = a2
                b1 = b2

    return minimum


tab = [(2, 4), (3, 6), (4, 8), (4, 7), (6, 7)]
print(find(tab, 2))