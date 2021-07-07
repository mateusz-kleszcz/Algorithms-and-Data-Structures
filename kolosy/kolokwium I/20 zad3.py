def partition(T, l, r):
    x = T[r]
    i = l
    for j in range(l, r):
        if T[j] < x:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quicksort(T, l, r):
    while l < r:
        p = partition(T, l, r)
        if (p - l) <= (r - p):
            quicksort(T, l, p - 1)
            l = p + 1
        else:
            quicksort(T, p + 1, r)
            r = p - 1


def check(T):
    quicksort(T, 0, len(T) - 1)
    for x in range(len(T)):
        p = 0
        q = len(T) - 1
        for i in range(len(T) - 1):
            if x == p:
                p += 1
                continue
            if x == q:
                q -= 1
                continue
            if p == q: return False
            if T[p] + T[q] == T[x]: break
            if T[p] + T[q] > T[x]: q -= 1
            if T[p] + T[q] < T[x]: p += 1
    return True


tab = [1, 3, -7, -4, -3, 4]
print(check(tab))