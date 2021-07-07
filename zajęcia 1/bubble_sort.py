def bubble(tab):
    n = len(tab)
    for i in range(n):
        isSwap = True
        for j in range(n - 1 - i):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
                isSwap = False
        if isSwap:
            break
    return tab


tab = [3, 5, 1, 11, 9, 64, 27, 18, 1]
print(bubble(tab))