def towers(tab):
    n = len(tab)
    tabIndexes = sorted(range(n), key=lambda x: tab[x][0])
    tab.sort()
    print(tab)
    range = (-float('inf'), float('inf'))

    prevEnd = -1
    for brick in tab:
        a, b = brick




tab = [[2, 4], [5, 7], [3, 6], [4, 5]]
towers(tab)