def is_more_than_half_same(tab):
    n = len(tab)
    counter = 1
    el = tab[0]
    for i in range(1, n):
        if tab[i] == el:
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            el = tab[i]
            counter = 1
    counter = 0
    for i in range(n):
        if tab[i] == el:
            counter += 1
    return True if n / 2 < counter else False


tab = [7, 7, 2, 4, 5, 7]
print(is_more_than_half_same(tab))