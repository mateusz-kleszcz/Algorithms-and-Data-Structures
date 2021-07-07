def kedane(tab):
    n = len(tab)
    max_curr = tab[0]
    max_total = tab[0]
    for x in range(1, n):
        max_curr = max(tab[x], max_curr + tab[x])
        max_total = max(max_curr, max_total)
    return max_total


def falisz(tab, left, right):
    #podział na mniejsze kawałki, n to długość kwałka, left right początek koniec, mid środek
    n = right - left + 1
    mid = left + (right - left) // 2
    #jak jest kawałek długości 0, to kończymy rekurencje, jak długości 1 to dodajemy wartość jak jest większa od 0
    if n == 0: return 0
    if n == 1: return max(0, tab[left])

    res_l = falisz(tab, left, mid)
    res_r = falisz(tab, mid + 1, right)

    span_l = span_r = 0
    partial = 0

    for i in range(mid, left - 1, -1):
        partial += tab[i]
        span_l = max(partial, span_l)
    partial = 0
    for i in range(mid + 1, right):
        partial += tab[i]
        span_r = max(partial, span_r)
    return max(res_l, res_r, span_l + span_r)


tab = [1, 2, 3, 4, -17, 2, 11, -30]