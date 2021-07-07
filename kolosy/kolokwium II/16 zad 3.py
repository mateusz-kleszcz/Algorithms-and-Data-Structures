def isPossible(tab):

    tab.sort()
    n = len(tab)

    if tab[0][0] != 0 or tab[n - 1][1] != 1:
        return False

    i = 0
    while tab[i][0] == 0:
        i += 1
    i -= 1
    end = tab[i][1]

    maxEnd = -1
    counter = 1

    while end != 1:
        while i != n and tab[i][0] < end:
            if tab[i][1] > maxEnd:
                maxEnd = tab[i][1]
            i += 1
        end = maxEnd
        counter += 1

    return counter


tab = [(0, 0.2), (0, 0.1), (0.05, 0.8), (0.3, 0.5), (0.1, 0.7), (0.75, 1), (0.9, 1)]
print(isPossible(tab))