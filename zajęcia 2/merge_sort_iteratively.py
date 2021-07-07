def merge(tab, left, right):
    pivot = (left + right) // 2
    # pomocniczy podział na 2 podzbiory
    n1 = pivot - left + 1
    t1 = [0] * n1
    for i in range(n1):
        t1[i] = tab[i + left]
    n2 = right - pivot
    t2 = [0] * n2
    for i in range(n2):
        t2[i] = tab[i + pivot + 1]
    # utworzenie wskaźników
    i = 0  # na początek pierwszej tablicy
    j = 0  # na początek drugiej tablicy
    q = left  # na początek tablicy wynikowej
    # scalanie dwóch zbiorów (biorę mniejszy z początkowych elementów tablicy t1, t2 i wstawiam go do tablicy wyjściowej)
    while i < n1 and j < n2:
        if t1[i] < t2[j]:
            tab[q] = t1[i]
            i += 1
        else:
            tab[q] = t2[j]
            j += 1
        q += 1
    # któryś zbiór może być dłuższy, jeżeli coś zostało to przepisuję do tablicy wynikowej
    while i < n1:
        tab[q] = t1[i]
        q += 1
        i += 1
    while j < n2:
        tab[q] = t2[j]
        q += 1
        j += 1


def merge_sort(tab):
    series_length = 2
    n = len(tab)
    while series_length <= n:
        for i in range(0, n, series_length):
            left = i
            right = min(left + series_length - 1, n - 1)
            if left != right:
                merge(tab, left, right)
        series_length *= 2
    return tab


tab = [123, 213, 1, 2, 4, 3, 1, 97, 11]
merge_sort(tab)
print(tab)