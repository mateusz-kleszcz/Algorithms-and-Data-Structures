def selection(tab):
    n = len(tab)
    for i in range(n):
        minValue = i
        for j in range(i + 1, n):
            if tab[j] < tab[minValue]:
                minValue = j
        tab[i], tab[minValue] = tab[minValue], tab[i]
    return tab


tab = [5, 3, 1, 11, 9, 64, 27, 18, 1]
print(selection(tab))