from random import randint, seed


def merge(tab, left, right, pivot):
    inv_count = 0
    #pomocniczy podział na 2 podzbiory
    n1 = pivot - left + 1
    t1 = [0] * n1
    for i in range(n1):
        t1[i] = tab[i + left]
    n2 = right - pivot
    t2 = [0] * n2
    for i in range(n2):
        t2[i] = tab[i + pivot + 1]
    #utworzenie wskaźników
    i = 0 # na początek pierwszej tablicy
    j = 0 # na początek drugiej tablicy
    q = left # na początek tablicy wynikowej
    # scalanie dwóch zbiorów (biorę mniejszy z początkowych elementów tablicy t1, t2 i wstawiam go do tablicy wyjściowej)
    while i < n1 and j < n2:
        if t1[i] <= t2[j]:
            tab[q] = t1[i]
            i += 1
        else:
            tab[q] = t2[j]
            inv_count += (n1 - i)
            j += 1
        q += 1
    # któryś zbiór może być dłuższy, jeżeli coś zostało to przepisuję do tablicy wynikowej
    while i < n1:
        tab[q] = t1[i]
        q += 1
        i += 1
    while i < n2:
        tab[q] = t2[i]
        q += 1
        i += 1
    return inv_count


def merge_sort(tab, left, right):
    inv = 0
    if left < right:
        pivot = (left + right) // 2
        inv += merge_sort(tab, left, pivot)
        inv += merge_sort(tab, pivot + 1, right)
        inv += merge(tab, left, right, pivot)
    return inv


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = merge_sort(T, 0, len(T) - 1)
print(T)
print("po sortowaniu    : T =", T)