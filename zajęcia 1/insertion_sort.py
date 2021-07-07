
def insertion(tab):
    n = len(tab)
    for i in range(1, n):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab


tab = [5, 3, 1, 11, 9, 64, 27, 18, 1]
print(insertion(tab))